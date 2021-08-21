Diabetes Model
================

Usage
----------

Clone this repository and run the following commands.

First, create a python virtual environment with

.. code-block:: bash

   > python3 -m venv .venv

Then you can activate it

.. code-block:: bash

   > source .venv/bin/activate

Install the package requirements

.. code-block:: bash


   > pip install -r requirements.txt

Initialize jupyterlab to see the notebooks and go to the `notebooks` folder to see the exploratory data analysis, data prep and modelling for this project.

.. code-block:: bash

   > jupyter lab --no-browser

Model scoring
----------------------------

You can use the command line interface in `cli.py` to score a new dataset:

.. code-block:: bash

   > python cli.py --input-data='data/raw/diabetes_data_upload.csv' --output-data='data/processed/diabetes_data_scored.csv'

The input-data must be a csv file.
