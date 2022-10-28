NICHD BSPC Training
===================

This repository hosts the source code and build infrastructure for a training website which is created and maintained by the Bioinformatics and Scientific Programming Core at NICHD, NIH.

The site can be found at **https://nichd-bspc.github.io/training**.

Contributions, suggestions, etc are very welcome. When you open a pull request or push changes to a pull request, the documentation will be automatically built and bundled into a zip file. This zip file  (found on the Actions tab -> job name -> "Artifacts" section) can be downloaded to inspect the results.

If you want to build docs locally, first create a `conda <https://docs.conda.io/en/latest/>`_ environment with the required dependencies::

  conda create -p ./env --file docs-requirements.txt --channel conda-forge

Then activate the environment (``conda activate ./env``), and run ``make html`` to build the docs.

The HTML docs will be found in the ``build/html`` directory.
