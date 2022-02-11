# UBC-MOAD Group Python Notes

This is a repo for Jupyter notebooks and notes in other forms about
Python usage, idioms, and techniques that the UBC-MOAD group thinks are
important, interesting, helpful, or just cool.

Please feel free to contribute your knowledge to existing notebooks,
or add new ones.
For the moment this is just a single directory to keep things simple;
perhaps we will categorize things into sub-directories if things get unweildy.

The notebooks will probably render just fine if you click on them in the
GitHub web interface.
You can also render them with things like the Javascript code-hiding button
on nbviewer at https://nbviewer.org/github/UBC-MOAD/PythonNotes/tree/master/

This repo is linked to the [#moad-python-notes](https://salishseacast.slack.com/archives/C01319S2YJW)
channel in the SalishSeaCast Slack workspace.
Update notifications will appear there whenever anything is pushed to this repo.
You can discuss things in the repo and ask questions there,
or you can open an [issue on GitHub](https://github.com/UBC-MOAD/PythonNotes/issues).
Issues have the advantage of keeping discussion threads together a little more seamlessly
than having to remember to reply to a thread instead of just posting the the Slack chanel,
but use whatever works best for you.
Issue notifications will also appear in the Slack channel.

If you want to run the notebooks in this repo locally:

  1. Clone the repo
  2. Create a conda environment (called `moad-python-notes`) containing the Python packages
     that the notebooks use with:

         cd PythonNotes
         conda env create -f environment.yaml

  3. Activate the conda environment with `conda activate moad-python-notes`
  4. Launch `jupyter lab` or `jupyter notebook`

If you are adding a new notebook that requires one or more Python packages that
are not already in the conda environment:

  1. Add the package(s) to the `dependencies:` list in `environment.yaml`
  2. Update your activated conda environment with:

         conda env update -f environment.yaml

  3. Commit your change to `environment.yaml` (separately, or with your new notebook),
     and push the changes to GitHub


## License

![https://www.apache.org/licenses/LICENSE-2.0](https://img.shields.io/badge/license-Apache%202-cb2533.svg)

The UBC EOAS MOAD Group PythonNotes notebooks and files are copyright 2020 – present by the
[UBC EOAS MOAD Group](https://github.com/UBC-MOAD/docs/blob/main/CONTRIBUTORS.rst)
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
