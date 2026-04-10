The Jupyter Notebooks in this directory are demonstrations of Python code used to collect model 
field values from the SalishSeaCast ERDDAP server to match ocean observations.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions under the links below are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [ScalingERDDAP-ObsMatching.ipynb](https://nbviewer.org/github/UBC-MOAD/PythonNotes/blob/main/erddap-obs-matching/ScalingERDDAP-ObsMatching.ipynb)  
    
    **Scaling ERDDAP Obs Matching**
    
    This notebook is a demonstration of a method to scale the collection SalishSeaCast model field values to match
    ocean observations for large numbers of observations.
    It builds on the foundation of the `BasicERDDAP-ObsMatching.ipynb` notebook in this directory to execute ERDDAP server requests in parallel.
    It uses `dask` to partition the `pandas.Dataframe` containing the observations into sections which can be processed concurrently
    and combined to produce the final dataframe that combines the model field values closest to the observations with the observations.
    The observations are assumed to be defined by a collection of 4d time-space coordinates in a `pandas.DataFrame`.
    (Those could, of course, be read from a CSV file.)

* ## [BasicERDDAP-ObsMatching.ipynb](https://nbviewer.org/github/UBC-MOAD/PythonNotes/blob/main/erddap-obs-matching/BasicERDDAP-ObsMatching.ipynb)  
    
    **Basic ERDDAP Obs Matching**
    
    This notebook is a demonstration of a basic recommended method to collect SalishSeaCast model field values to match
    ocean observations.
    It uses `xarray` to access the SalishSeaCast model datasets via the ERDDAP server.
    The observations are assumed to be defined by a collection of 4d time-space coordinates in a `pandas.DataFrame`.
    (Those could, of course, be read from a CSV file.)
    The model field values closest to the observations are combined with the observations to create a consolidated
    `pandas.DataFrame`.



## Using the Notebooks

* Install [Pixi](https://pixi.prefix.dev/latest/) if you have not already done so

* Install the `erddap-obs-matching` environment with:
    ```bash
    cd PythonNotes
    pixi install -e erddap-obs-matching
    ```

* If you are using VSCode:

  * Install the [Pixi Code extension](https://marketplace.visualstudio.com/items?itemName=renan-r-santos.pixi-code) 
    if you have not already done so

  * Open a notebook

  * Use the `Select Kernel` button to select `.pixi/envs/erddap-obs-matching/bin/python`

* If you want to use Jupyter Lab in a browser,
  launch it with:

    ```bash
    pixi run -e erddap-obs-matching jupyter lab
    ```


## License

These notebooks and files are copyright 2013 – present by the
[SalishSeaCast Project Contributors](https://github.com/SalishSeaCast/docs/blob/main/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
