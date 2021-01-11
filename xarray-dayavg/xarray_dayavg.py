"""Example of using xarray.open_mfdataset() and dask to aggregate SalishSeaCast results
from a collection of sequential dates.

Specifically, this example calculates daily averaged fields for phytoplankton variables
at each domain grid point for sring/summer of a year.

This code will take hundreds of seconds to run.
The goal of code like this is to produce an intermediate results file that can be loaded
in subsequent steps of processing pipelines. You shouldn't need to run code like this
every time you run some analysis.

**Note:** If you are doing something other than calculating daily averaged fields for
phytoplankton variables at each domain grid point, you need to tune things like:
* list of files to read
* chunking to use to load the datasets
* temporal and spatial slicing of the dataset
* the aggregation operation
* the number of workers to distribute the dask task graph to
* chunking to use to store the intermediate results dataset

Things that I don't understand about what this code is doing:
* The result dataset includes the variable ammonium despite in being in the list of
  dropped variables
* RuntimeWarnings that seem to be about NaNs are raised despite skipna=True
  in the .mean() call:
  dask/array/numpy_compat.py:40: RuntimeWarning: invalid value encountered in true_divide
* The chunking of the output file is (number_of_days/4, 10, 225, 100);
  e.g. for Mar: (8, 10, 225, 100), for Mar-Apr: (13, 10, 225, 100);
  i.e. the dimension sizes of the day average dataset are being divided by 4
"""
import math
import sys
import time
from pathlib import Path

import arrow
import xarray


def main(start_date, end_date, num_workers):
    t_start_total = time.time()

    t_start = time.time()
    hindcast1905_path = Path("/results2/SalishSea/hindcast.201905/")
    # assuming that start_date and end_date are in the same year
    pattern = f"*{arrow.get(start_date).format('YY')}/SalishSea_1h_*_ptrc_T.nc"
    ds_files = sorted(hindcast1905_path.glob(pattern))
    print(f"calc list of dataset files to open: {time.time() - t_start} s")

    # chunking is related to both how the files are stored, and how we will use them
    # it is super-important to get this tuned correctly!
    chunks = {
        "time_counter": 24,
        "deptht": 40,
        "y": 898,
        "x": 398,
    }

    # don't process variables we don't need in the dataset we are producing
    drop_vars = {
        "axis_nbounds",
        "nvertex",
        "nav_lat",
        "nav_lon",
        "bounds_lon",
        "bounds_lat",
        "area",
        "deptht_bounds",
        "time_centered",
        "time_centered_bounds",
        "time_counter_bounds," "ammonium",
        "microzooplankton",
        "nitrate",
        "silicon",
        "dissolved_organic_nitrogen",
        "particulate_organic_nitrogen",
        "biogenic_silicon",
        "mesozooplankton",
    }

    # start building the dask task graph
    t_start = time.time()
    ds = xarray.open_mfdataset(ds_files, chunks=chunks, drop_variables=drop_vars)
    print(f"load metadata via open_mfdataset(): {time.time() - t_start} s")

    # how big are our chunks? aiming for 100 Mb to 1 Gb
    print(
        f"chunk size: {math.prod(chunks.values()) * ds.diatoms.dtype.itemsize /1024/1024/1024} Gb"
    )

    # select temporal (and spatial, if needed) slice of dataset before aggregation operations
    t_start = time.time()
    ds = ds.sel(time_counter=slice(start_date, end_date))
    print(f"temporal/spatial slicing: {time.time() - t_start} s")

    # calculate the day averages
    # this does some processing, and adds more tasks to the graph
    t_start = time.time()
    day_avgs = ds.resample(time_counter="D").mean(
        dim="time_counter", skipna=True, keep_attrs=True
    )
    print(f"calc day averages: {time.time() - t_start} s")

    # Call the .load() method to trigger the actual work that has been built up in the dask
    # task graph above
    # Use the processes scheduler instead of the default threads scheduler so that we start
    # multiple Python interpreters on multiple cores to do the work;
    # that configuration is better suited to this kind of workload than using threads
    # Choose a sane, reasonable, and polite number of workers; 16 is okay if nothing else is
    # running or likely to run on salish, but 8 is the max when nowcast-dev is running
    # or likely to start, or when other people are working
    t_start = time.time()
    day_avgs.load(scheduler="processes", num_workers=num_workers)
    print(f"calc the task graph: {time.time() - t_start} s")

    # Dump the result to an intermediate results netCDF file that will be read at start of
    # next step in pipeline; no need to recalculate day averages often.
    # Use zlib deflation of dataset variables to limit disk space sprawl;
    # ~80% reduction in file size
    t_start = time.time()
    encoding = {var: {"zlib": True} for var in day_avgs.data_vars}
    day_avgs.to_netcdf(f"{arrow.get(start_date).year}_dayavgs.nc", encoding=encoding)
    print(f"write day avgs to .nc file: {time.time() - t_start} s")

    print(f"total time: {time.time() - t_start_total} s")


if __name__ == "__main__":
    # This is extremely lame command-line args processing
    start_date, end_date, num_workers = sys.argv[1:]
    num_workers = int(num_workers)
    main(start_date, end_date, num_workers)
