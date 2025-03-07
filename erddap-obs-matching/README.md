The Jupyter Notebooks in this directory are demonstrations of Python code used to collect model 
field values from the SalishSeaCast ERDDAP server to match ocean observations.

The links below are to static renderings of the notebooks via
[nbviewer.org](https://nbviewer.org/).
Descriptions under the links below are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ## [BasicERDDAP-ObsMatching.ipynb](https://nbviewer.org/github/UBC-MOAD/PythonNotes/blob/main/erddap-obs-matching/BasicERDDAP-ObsMatching.ipynb)  
    
    **Basic ERDDAP Obs Matching**
    
    This notebook is a demonstration of a basic recommended method to collect SalishSeaCast model field values to match
    ocean observations.
    It uses `xarray` to access the SalishSeaCast model datasets via the ERDDAP server.
    The observations are assumed to be defined by a collection of 4d time-space coordinates in a `pandas.DataFrame`.
    (Those could, of course, be read from a CSV file.)
    The model field values closest to the observations are collected in an `xarray.Dataset` that is converted to a
    `pandas.DataFrame` at the end of the notebook.



## License

These notebooks and files are copyright 2013 – present by the
[SalishSeaCast Project Contributors](https://github.com/SalishSeaCast/docs/blob/main/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file in this repository for details of the license.
