# Data for PPI4SD

PPI4SD uses secondary data on development indicators, extracted from various sources. The data can be divided into two levels: *national* and *sub-national*. 

### New SDG 18
It should be noted that we have created an additional SDG (number 18) to separate the topic of *peace and justice* from *strong institutions* in SDG 16. Thus, in this project, SDG 16 contains indicators of *peace and justice*, while SDG 18 covers *strong institutions*. This separation is important in the Mexican context, there governance issues may represent challenges that are not necessarily directly related to *peace and justice*.

## National Level Data
National level data consists of development indicators for the entire country of Mexico, and they have been obtained from the following sources:

* [United Nations Global SDG Database](https://unstats.un.org/sdgs/indicators/database/) (UN)
* [World Bank Sustainable Development Goals Database](http://datatopics.worldbank.org/sdgs/) (WDI)
* [World Bank Povery and Equity Indicators](http://povertydata.worldbank.org/poverty/home/) (WBP)
* [Worldwide Governance Indicators](https://datacatalog.worldbank.org/dataset/worldwide-governance-indicators) (WGI)
* [Global Competitiveness Report Indicators](https://knoema.com/atlas/sources/WEF) (GCI)
* [Observatory of Economic Complexity](https://atlas.media.mit.edu/en/) (OEC)

Most of the data comes from the United Nations Global SDG Database, which is the official source of the SDGs. However, in many cases, this source is insufficient to cover all the 17 SDGs. For this reason, we have complemented the official source with indicators from other databases, and classified them into the SDGs.

## Data Structure
The national level data covers the period 2005-2017. It is in the 

| 2005 | ... | 2017 | goal | target | source | countryCode | seriesCode | seriesName | instrumental | reverse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .552 | ... | .671 | 17 | 17.2 | UN | MEX | 17.4.1_1 | Debt service as a proportion of exports of goods and services (%) | 1 | 1 |
| .043 | ... | .236 | 5 | NA | GCI | MEX | EOSQ088 | Ease of access to loans | 1 | 1 |





