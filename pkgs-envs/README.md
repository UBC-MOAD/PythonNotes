# Python Packages and Environments Notebooks & Slides

The notebooks in this directory are from MOAD group discussions about Python packages and environments
that Doug has lead over the years.
They reflect the evolution of the Python packaging and environments ecosystem,
its tools,
and the recommended workflows for the group.
The notebooks can be viewed as slideshows by using the 
[jupyterlab_rise](https://jupyterlab-contrib.github.io/rise.html)
slide show extension for Jupyter Lab.

If you are working in an up to date clone of the 
[UBC-MOAD/PythonNotes repo](https://github.com/UBC-MOAD/PythonNotes),
you can run the slideshow locally.
To do so:
* Install [Pixi](https://pixi.prefix.dev/latest/) if you have not already done so
* Install the `pkgs-envs` environment with:
```bash
cd PythonNotes
pixi install -e pkgs-envs
```
* Launch `jupyter lab` or `jupyter notebook` with:

    ```bash
    pixi run -e pkgs-envs jupyter lab
    ```
  or
    ```bash
    pixi run -e pkgs-envs jupyter notebook
    ```

  then open the notebook you're interested in.
* Or, launch a specific notebook directly with a command like:
    ```bash
    pixi run -e pkgs-envs jupyter lab pkgs-envs/PythonPkgsEnvsSlides-2026.ipynb
    ```
* use `Alt+r` or the slideshow emoji toolbar button to start/stop the slideshow mode
* use `Space` and `Shift+Space` to navigate forward and backward through the slide cells