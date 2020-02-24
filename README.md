# Policy Priority Inference for Sustainable Development (PPI4SD)

This is the public repository for the code and data of the project: *Policy Priority Inference for Sustainable Development* (PPI4SD). The project stems from the research program: [*Policy Priority Inference*](https://www.turing.ac.uk/research/research-projects/policy-priority-inference), developed at [The Alan Turing Institute](https://www.turing.ac.uk) by [Omar Guerrero](https://oguerr.com) and [Gonzalo Castañeda](https://www.cide.edu/nosotros/comunidad/profesores/perfil/?id=25). PPI4SD has been sponsored by the [United Nations Development Program for Latin-America and the Caribbean](http://www.latinamerica.undp.org/), and has been developed in collaboration with the Mexican [National Laboratory of Public Policy](https://www.lnpp.mx).

In this repository you will find the necessary data and code to replicate the analysis presented in the different reports produced by PPI4SD. The different pages in this Wiki provide all the necessary references to the official documentation from which the data were constructed. Likewise, here you will find all the code and documentation required to analyze the data through the project's methodology. Should you have any further inquiries please contact Omar Guerrero at oguerrero@turing.ac.uk.


## Getting started
The following list of activities is a suggestion on *how to get started* with the PPI4SD model. 

### Before you start: become familiar with the model
PPI4SD is an economic model and we therefore strongly encourage you to read the scientific work behind the model before you try to run it on your own. The following two resources should help you understand the model. 
1. [How do governments determine policy priorities? Studying development strategies through spillover networks](http://www.sciencedirect.com/science/article/pii/S0167268118302026). Gonzalo Castañeda, Florian Chávez-Juárez, Omar A. Guerrero. *Journal of Economic Behavior & Organization*, Volume 154, 2018,Pages 335-361. Find [here](https://arxiv.org/abs/1902.00432) a working paper version. 
2. **Inferencia de Prioridades de Política para el Desarrollo Sostenible. Reporte Metodológico** (*Link will be available soon*), Gonzalo Castañeda and Omar A. Guerrero. Methodological paper describing the adaptation of the core model to the Sustainable Development Goals (SDG). In Spanish. 
4. **Inferencia de Prioridades de Política para el Desarrollo Sostenible: Una Aplicación para el Caso de México** (*Link will be available soon*). Gonzalo Castañeda and Omar A. Guerrero. Document with a country level analysis for Mexico. Many of the code examples in this repository stem from this study. 
4. **Inferencia de Prioridades de Política para el Desarrollo Sostenible: El Caso Sub-Nacional de México** (*Link will be available soon*). Gonzalo Castañeda and Omar A. Guerrero. Document with a sub-national level analysis for Mexico. Many of the code examples in this repository stem from this study. 

### Running PPI with preloaded data and settings
First, we suggest that you run the PPI4SD model with the data and settings used in the above references. In the folder [/Code/Examples](/Code/Examples) you fill find 5 commented [Jupyter Notebooks](https://realpython.com/jupyter-notebook-introduction/) with different examples on how to use the model: 
1. [Example_1_data.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_1_data.ipynb): This notebook introduced the input data and visualised this data to better understand it. PPI4SD is _not_ used in this notebook. 
2.  [Example_2_PPI.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_2_PPI.ipynb): This notebook reproduces a single run of the PPI4SD using the national data for Mexico. The purpose of this notebook is to see how a single run works and to analyse how the results change when you play around with the input data. Note that a single run should never be used to publish results. 
3. [Example_3_Monte_Carlo.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_3_Monte_Carlo.ipynb): This notebook reproduces the main results of the national study for Mexico mentioned above. It illustrates how to batch-run the model 1000 times and obtain the combined results of all the runs. 
4. [Example_4_estimation.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_4_estimation.ipynb): in this notebook you can learn how to estimate the growth factors. This step is required before running PPI4SD if you wish to use your own data. 
5. [Example_5_calibration.ipynb](https://github.com/oguerrer/PPI4SD/blob/master/Code/Examples/Example_5_calibration.ipynb): This notebook shows how to calibrate number of periods for convergence. Similar to exercise 4, this is only needed if you run the model with your own data. 

### Preparing your own analyses
Once you are sufficiently familiar with the model and the code, you can start running your own models. In the folder [/Subnational_data/](/Subnational_data) you can find all necessary files and data to run the analysis for any given State in Mexico. 

If you wish to start from zero, we recommend you follow the data preparation instructions in the technical report mentioned above. Once you have the data ready, you can estimate the dependency network with your preferred method. For the above-mentioned reports, the R-package [sparsebn](https://cran.r-project.org/web/packages/sparsebn/index.html) has been used. 

