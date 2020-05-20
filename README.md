# Policy Priority Inference for Sustainable Development (PPI4SD)

This is the public repository for the code and data of the project: *Policy Priority Inference for Sustainable Development* (PPI4SD). The project stems from the research program: [*Policy Priority Inference*](https://www.turing.ac.uk/research/research-projects/policy-priority-inference), developed at [The Alan Turing Institute](https://www.turing.ac.uk) by [Omar Guerrero](https://oguerr.com) and [Gonzalo Castañeda](https://www.cide.edu/nosotros/comunidad/profesores/perfil/?id=25). PPI4SD has been sponsored by the [United Nations Development Program for Latin-America and the Caribbean](http://www.latinamerica.undp.org/), and has been developed in collaboration with the Mexican [National Laboratory of Public Policy](https://www.lnpp.mx).

In this repository you will find the necessary data and code to replicate the analysis presented in the different reports produced by PPI4SD. The different pages in this repository provide all the necessary references to the official documentation from which the data were constructed. Likewise, here you will find all the code and documentation required to analyze the data through the project's methodology. Should you have any further inquiries please contact Omar Guerrero at oguerrero@turing.ac.uk.


## Getting started
The following activities are recommended to *get started* with the PPI4SD. 

### Before you start: become familiar with the model
PPI4SD is an economic model, so reading the scientific work behind the model is encouraged. The examples in this repository are based on the following resources.

1. [How do governments determine policy priorities? Studying development strategies through spillover networks](http://www.sciencedirect.com/science/article/pii/S0167268118302026). Gonzalo Castañeda, Florian Chávez-Juárez, Omar A. Guerrero. *Journal of Economic Behavior & Organization*, Volume 154, 2018,Pages 335-361. Open-access pre-print available [here](https://arxiv.org/abs/1902.00432). 
2. [Inferencia de Prioridades de Política para el Desarrollo Sostenible. Reporte Metodológico](https://www.lnpp.mx/publicacion/1-inferencia-de-prioridades-de-politica-publica-para-el-desarrollo-sostenible-reporte-metodologico/), Gonzalo Castañeda and Omar A. Guerrero. Methodological paper describing the adaptation of the core model to the Sustainable Development Goals (SDG). In Spanish. 
3. [Inferencia de Prioridades de Política para el Desarrollo Sostenible: Una Aplicación para el Caso de México](https://www.lnpp.mx/publicacion/inferencia-de-prioridades-de-politica-publica-para-el-desarrollo-sostenible-el-caso-subnacional-de-mexico-2/). Gonzalo Castañeda and Omar A. Guerrero. Document with a country level analysis for Mexico. Many of the code examples in this repository stem from this study. 
4. [Inferencia de Prioridades de Política para el Desarrollo Sostenible: El Caso Sub-Nacional de México](https://www.lnpp.mx/publicacion/inferencia-de-prioridades-de-politica-publica-para-el-desarrollo-sostenible-el-caso-subnacional-de-mexico/). Gonzalo Castañeda and Omar A. Guerrero. Document with a sub-national level analysis for Mexico. Many of the code examples in this repository stem from this study. 
5. [Policy Priority Inference: A Computational Method for the Analysis of Sustainable Development](http://ssrn.com/abstract=3604041). While all the reports were prepared in Spanish, we have prepared a research paper in English that builds on the first two reports.


### Running PPI with preloaded data and settings

First, we suggest running PPI4SD with the data and settings used in the aforementioned references.
In the folder [/Code/Examples](/Code/Examples), you will find 5 annotated [Jupyter Notebooks](https://realpython.com/jupyter-notebook-introduction/) with different examples on how to use the model:

1. [Example_1_data.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_1_data.ipynb): This notebook introduces the input data and visualizations. PPI4SD is _not_ used in this notebook. 

2.  [Example_2_PPI.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_2_PPI.ipynb): This notebook shows how to perform a single run of PPI4SD using national-level data from Mexico.
The purpose of this notebook is to show how a single run works and to analyse how the results when changing the input data.
Note that a single run is not representative of the model outputs. 

3. [Example_3_Monte_Carlo.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_3_Monte_Carlo.ipynb): This notebook reproduces the main results of the national study for Mexico mentioned above.
It illustrates how to batch-run the model 1,000 times and to obtain the combined results of all the simulations. 

4. [Example_4_estimation.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_4_estimation.ipynb): This notebook demonstrate how to estimate the growth factors.
This step is required before running PPI4SD if you wish to use your own data.
Notebook 3 uses pre-estimated growth factors.

5. [Example_5_calibration.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_5_calibration.ipynb): This notebook shows how to calibrate the number of periods for which the simulations will run.
Similar to exercise 4, this is only needed if you run the model with your own data. 


### Preparing your own analyses

Once you are sufficiently familiar with the model and the code, you can start running your own models.
In the folder [/Subnational_data/](/Subnational_data) you can find all necessary files and data to run the analysis for all the Mexican states (there are 32). 

If you wish to start from zero, we recommend you follow the data preparation instructions in the technical report.
Once the data has been properly pre-processed, you can estimate the conditional-dependency network with your preferred method.
In the above-mentioned reports, the R-package [sparsebn](https://cran.r-project.org/web/packages/sparsebn/index.html) has been used. 

