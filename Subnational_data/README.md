# Subnational Data

These data were constructed by the [National Laboratory of Public Policy (LNPP)](https://www.lnpp.mx) using state level secondary data from various sources.
The data includes the period from 2005 to 2018, although most series stop in 2016. 
In contrast with the national data, SDG 16 was not sub-divided.


## Development Indicators
The subnational level data consist of development indicators collected from various sources; generally, from government agencies or from the Mexican Statistical Bureau.
These data cover the period 2006-2018, with each year coded into a column in a table. However, not all indicators have full coverage.
Therefore, the report prepared for a sub-national analysis employs a sample of these data.

We provide two versions of these data: *normalized* and *raw*.
In the normalized version, the indicators have been mapped into the interval [0,1], where zero and one are the lowest and highest levels respectively (see the technical report for more details on this normalization).
In addition, the normalized indicators they have been subjected to an *inversion* procedure in order to guarantee that higher levels represent better outcomes.
The raw version has the original values prior to the normalization procedure.
Both datasets can be found in the CSV-formatted files: `dataSubnacionalForAnalysis.csv` and `dataSubnacionalForAnalysis_normalized.csv`.
The following table provides an example of the data structure.


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


## Network

## Growth Factors

## Development Goals

### Goals from the OECD Members

### Governance Parameters

### Goals from Official Documents

## SDG Budgeting

## References
