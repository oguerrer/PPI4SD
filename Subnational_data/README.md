# Subnational Data

These data were constructed by the [National Laboratory of Public Policy (LNPP)](https://www.lnpp.mx) using state level secondary data from various sources.
The data includes the period from 2005 to 2018, although most series stop in 2016. 
In contrast with the national data, SDG 16 was not sub-divided.


## Development Indicators
The subnational level data consist of development indicators collected from various sources; generally, from government agencies or from the Mexican Statistical Bureau.
These data cover the period 2006-2018, with each year coded into a column in a table. However, not all indicators have full coverage.
Therefore, the report prepared for a subnational analysis employs a sample of these data.

We provide two versions of these data: *normalized* and *raw*.
In the normalized version, the indicators have been mapped into the interval [0,1], where zero and one are the lowest and highest levels respectively (see the technical report for more details on this normalization).
In addition, the normalized indicators they have been subjected to an *inversion* procedure in order to guarantee that higher levels represent better outcomes.
The raw version has the original values prior to the normalization procedure.
Both datasets can be found in the CSV-formatted files: `dataSubnacionalForAnalysis.csv` and `dataSubnacionalForAnalysis_normalized.csv`.
The following table provides an example of the data structure.
Since indicator coverage varies slighly between states, we provide state-specific data files in the folders `Subnational_data/samples_normalized` and `Subnational_data/samples_raw`.
These files are consistent (same number of indicators and same order) with the complementary data on the estimated growth factors and interdependency networks.


| 2006 | ... | 2016 | 2017 | 2018 | goal | target | source | countryCode | seriesCode | seriesName | instrumental | reverse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |... | 13.03 | | 11.26 | 1 | 1.1 | CONEVAL | CHP | 3 | Porcentaje de poblacion vulnerable por ingresos | 1 | 1 |
| |... |6.79 | | 7.76| 1|1.1|CONEVAL|CMX|3|Porcentaje de poblacion vulnerable por ingresos|1|1|
|82.40 | ...|107.60|||16.1|16.1|ENVIPE|AGU|185|Tasa de robo a negocio|1|1|
|105.86|...|182.22|||16.1|16.1|ENVIPE|BCN|185|Tasa de robo a negocio|1|1|

In the raw data, that missing values appear empty left empty.
In the normalized version, empty cells sorunded by observations (with value to the left and right) have been imputed through linear interpolation.
Besides the columns representing the years of the observations, there are additional attributes that we explain below:

* `goal`: an unofficial SDG classification developed by the NLPP
* `target`: the target to which the indicator belongs within its SDG. Targets are defined only for indicators from the United Nations SDG Database and from the World Bank SDG Database.
* `stateCode`: a 3-character code of the corresponding state.
* `seriesCode`: the code of the indicator as it appears in its original database. If there was no code assigned by the data supplier, then one was created (e.g. for most indicators in SDG 1).
* `instrumental`: a binary variable indicating whether the topic of the indicator is *instrumental*, *i.e.* that it has specific policy instruments and dedicated resources (see technical report for more details).
* `reverse`: a binary variable saying if the indicator needs to be reversed so that a higher value represents a better outcome. In the normalized data, all the indicators the relevant indicators have been reversed. In the raw data this is not the case.
* `sdg`: the official SDG to which the indicator belongs (1, 2, ..., 16, 17)
* `seriesNameSpanish`: the description of the indicator in Spanish.
* `sourceNameSpanish`: the name in Spanish of the organization from which the indicators were obtained.


## Networks
The networks of interdependencies between development indicators can be estimated by the user through various methods. [Ospina-Forero et al. (2019)](http://dx.doi.org/10.2139/ssrn.3385362) provide a comprehensive survey.
For this project, the method of Learning Sparse Bayesian Networks from High-Dimensional Data by [Aragam et al. (2017)](https://github.com/itsrainingdata/sparsebn) was employed.
This repository provides the the network that was estimated for each state.
The folder `Subnational_data/networks` contains squared matrices, each one corresponding to a state network, where each row and each column represents a development indicator.
The rows and columns are ordered in the same fashion as in the files in folders `Subnational_data/samples_normalized` and `Subnational_data/samples_raw`.
All these networks were constructed following the same procedures as in the national report (see the [`National_data`](https://github.com/oguerrer/PPI4SD/tree/master/National_data) folder of this repository).

## Growth Factors
To facilitate replicability, this repository provides the estimated growth factors of each state in the folder `Subnational_data/alphas`.

## Governance Parameters
Due to the recent construction of governance indicators at the subnational level, it was decided to use national-level governance indicators.
In particular, the parameters capturing the quality of the monitoring mechanisms and of the rule of law are provided in the file `National_data/governance_params.csv`.
It consists of a vector where the first element corresponds to monitoring and the second to the rule of law.
The technical report provides the details on how these data were obtained.

## Development Goals
In the subnational report, prospective analyses were conducted using development goals that the NLPP and the UNDP-Mexico elicited from states' representatives and from official documents such as state development plans.
These goals were quantified in terms of growth rates for each of the indicators built by the NLPP.
In total, five states contributed with such information: Chiapas, Jalisco, the State of Mexico, Nuevo León, and Yucatán.
The folder `Subational_data/goals` provides the data files, listing the `id` of each indicator and the corresponding growth rate.
For example, if indicator 32 has a growth rate of 0.23, it means that, according to official documents, the state's aspiration is for indicator 32 to grow in 32% with respect to its baseline level.

## References

[1] Ospina-Forero, Luis and Castañeda Ramos, Gonzalo and Guerrero, Omar A, Estimating Networks of Sustainable Development Goals (May 9, 2019). Available at SSRN: https://ssrn.com/abstract=3385362 or http://dx.doi.org/10.2139/ssrn.3385362 

[2] Aragam, B., Gu, J., and Zhou, Q. (2017). Learning large-scale Bayesian networks with the sparsebn package. arXiv: 1703.04025.
