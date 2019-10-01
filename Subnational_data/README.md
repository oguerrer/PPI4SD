# Subnational Data

These data were constructed by the [National Laboratory of Public Policy (LNPP)]{https://www.lnpp.mx) using state level secondary data from various sources . The data includes the period from 2005 to 2018, although most series stop in 2016. 


## Adjustments to official SDG
We had to make a few adjustments to the [official categories](https://www.un.org/development/desa/disabilities/envision2030.html) of sustainable development goals (SDG) for the subnational case. In some cases we divided a goal into various to better capture the different aspects of a general goal. This will allow the model to be more precise about which element of the goal requires more attention. On the contrary, due to data limitations, we had to merge several environmental goals into a single large goal. The details of the changes are highlighted in the following list: 

* Goal 8: Decent Work and Economic Growth was divided into two: 
	* Goal 8.1 Economic Growth
	* Goal 8.2 Decent work
* Goal 9: Industry, Innovation and Infrastructure was divided into three: 
	* Goal 9.1: Innovation and industry
	* Goal 9.2: Infrastructure
	* Goal 9.3: Financial infrastructure
* Goal 16: Peace and Justice Strong Institutions was divided into:
	* Goal 16.1: Piece and Justice
	* Goal 16.2: Strong Institutions
* The following goals were merged into a single goal MA (environment): 
	* Goal 7: Affordable and Clean Energy
	* Goal 12: Responsible Consumption and Production
	* Goal 13: Climate Action
	* Goal 14: Life Below Water
	* Goal 15: Life on Land
	

## Development Indicators
The subnational level indicators consist of development indicators collected from various sources, generally from the responsible government agencies or the Mexican Statistical Bureau. 

These data cover the period 2006-2018, with each year coded into a column in a table. 

We provide two versions of these data: *normalized* and *raw*. In the normalized version, the indicators have been mapped into the interval [0,1], where zero and one are the lowest and highest values for that indicator (see the technical report for more details on this normalization). The raw version has the original values without normalization. Both datasets can be found in the CSV-formatted files: `dataSubnacionalForAnalysis.csv` and `dataSubnacionalForAnalysis_normalized.csv`. The following table provides an example of the structure.

| 2005 | ... | 2017 | goal | target | countryCode | seriesCode | seriesName | instrumental | reverse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .552 | ... | .671 | 17 | 17.2 | MEX | 17.4.1_1 | Debt service as a proportion of exports of goods and services (%) | 1 | 1 |
| .043 | ... | .236 | 5 | NA | MEX | EOSQ088 | Ease of access to loans | 1 | 1 |


| 2006 | ... | 2016 |
| --- | --- | --- |
| A | B | C |


2006|...|2016|2017|2018|goal|target|source|countryCode|seriesCode|seriesName|instrumental|reverse|
 --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- |
|13.03||11.26|1|1.1|CONEVAL|CHP|3|Porcentaje de poblacion vulnerable por ingresos||
|6.79||7.76|1|1.1|CONEVAL|CMX|3|Porcentaje de poblacion vulnerable por ingresos||
|82.40 | ... ||107.60|||16.1|16.1|ENVIPE|AGU|185|Tasa de robo a negocio||
|105.86|182.22|||16.1|16.1|ENVIPE|BCN|185|Tasa de robo a negocio||

Besides the columns representing the years of the observations, there are additional attributes that we explain below:

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
