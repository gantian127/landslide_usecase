# Data Component Use Case for Landslide Susceptibility Calculation
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/gantian127/landslide_usecase/blob/master/LICENSE.txt)


This repository includes a [Jupyter Notebook](landslide_puertorico.ipynb) 
which demonstrates how to use several [CSDMS Data Components](https://csdms.colorado.edu/wiki/DataComponents) to download 
topography and soil datasets to calculate the landslide susceptibility for a study area in Puerto Rico when Hurricane 
Maria hit the island on September 20th, 2017.

This Jupyter Notebook is part of the work for a research paper 
"CSDMS Data Components: data-model integration tools for Earth surface processes modeling".


### Notebook Citation
Gan, T., Campforts, B., Tucker, G. E., Overeem, I. (2023). Data Component Use Case for Landslide Susceptibility 
Calculation, HydroShare, https://www.hydroshare.org/resource/df5fa2f5d1b74be4bf0a049e1e59889c/


### Run the Notebook
You can choose the following methods to run this Jupyter Notebook: 

#### Method 1: HydroShare
Please go to the [HydroShare Resource](https://www.hydroshare.org/resource/df5fa2f5d1b74be4bf0a049e1e59889c/) 
and follow the instruction in the **"Abstract"** section to run this notebook.

#### Method 2: CSDMS
Please go to the [CSDMS EKT Lab](https://csdms.colorado.edu/wiki/Lab-0031) 
and follow the instruction in **"Lab notes"** section to run this notebook.


#### Method 3: Local PC
Please first download all the files from this repository and have 
[conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on the local PC.
Then, use the following commands to create a virtual environment and launch the Jupyter Notebook.
```
$ cd landslide_usecase
$ conda env create --file=environment.yml
$ conda activate landslide_usecase
$ jupyter notebook
```
