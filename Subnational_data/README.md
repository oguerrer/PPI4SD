# Subnational Data

These data were constructed by the [National Laboratory of Public Policy (LNPP)](https://www.lnpp.mx) using state level secondary data from various sources. The data includes the period from 2005 to 2018, although most series stop in 2016. 


## Development Indicators
The subnational level indicators consist of development indicators collected from various sources, generally from the responsible government agencies or the Mexican Statistical Bureau. 

These data cover the period 2006-2018, with each year coded into a column in a table. 

We provide two versions of these data: *normalized* and *raw*. In the normalized version, the indicators have been mapped into the interval [0,1], where zero and one are the lowest and highest values for that indicator (see the technical report for more details on this normalization). The raw version has the original values without normalization. Both datasets can be found in the CSV-formatted files: `dataSubnacionalForAnalysis.csv` and `dataSubnacionalForAnalysis_normalized.csv`. The following table provides an example of the structure.


| 2006 | ... | 2016 | 2017 | 2018 | goal | target | source | countryCode | seriesCode | seriesName | instrumental | reverse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |... | 13.03 | | 11.26 | 1 | 1.1 | CONEVAL | CHP | 3 | Porcentaje de poblacion vulnerable por ingresos | 1 | 1 |
| |... |6.79 | | 7.76| 1|1.1|CONEVAL|CMX|3|Porcentaje de poblacion vulnerable por ingresos|1|1|
|82.40 | ...|107.60|||16.1|16.1|ENVIPE|AGU|185|Tasa de robo a negocio|1|1|
|105.86|...|182.22|||16.1|16.1|ENVIPE|BCN|185|Tasa de robo a negocio|1|1|

Note that missing values should be left empty in the csv file. Besides the columns representing the years of the observations, there are additional attributes that we explain below:

* `goal`: the SDG to which the indicator belongs 
* `target`: the target to which the indicator belongs within its SDG. 
* `source`: the agency from which we obtained the information. 
* `countryCode`: the 3-digit ISO code of the relevant federal entity (estado).
* `seriesCode`: an internal code for each data series. Each code is unique.
* `seriesName`: the description of the indicator as provided by the original data.
* `instrumental`: a binary variable indicating whether we consider that the topic of the indicator is *instrumental*, *i.e.* that is has specific policy instruments and dedicated resources (see technical report for more details).
* `reverse`: a binary variable saying if the indicator needs to be reversed so that a higher value represents a better outcome. In the normalized data, all the indicators that required reversion have been reversed. In the raw data this is not the case.


## Network

## Growth Factors

## Development Goals

### Goals from the OECD Members

### Governance Parameters

### Goals from Official Documents

## SDG Budgeting

## References
