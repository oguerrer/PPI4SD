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

Most of the data comes from the United Nations Global SDG Database, which is the official source of the SDGs. However, in many cases, this source is insufficient to cover all the 17 SDGs. For this reason, we have complemented the official source with indicators from other databases and classified them into the SDGs.

### Data Structure of National Data
The national level data covers the period 2005-2017, with each year being a column in a table. We provide two versions of it: *normalized* and *raw*. In the normalized version, the indicators have been mapped into the interval [0,1], where zero and one are the lowest and highest values for that indicator, obtained from a larger sample of countries and years (see the technical report for more details). The raw version has the original values. Both datasets can be found in the CSV-formatted files: `sample_data_norm.csv` and `sample_data_raw.csv`. The following table provides an example of the structure.

| 2005 | ... | 2017 | goal | target | source | countryCode | seriesCode | seriesName | instrumental | reverse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .552 | ... | .671 | 17 | 17.2 | UN | MEX | 17.4.1_1 | Debt service as a proportion of exports of goods and services (%) | 1 | 1 |
| .043 | ... | .236 | 5 | NA | GCI | MEX | EOSQ088 | Ease of access to loans | 1 | 1 |

Besides the columns representing the years of the observations, there are aditional attributes that we explain bellow:

* `goal`: the SDG to which the indicator belongs (1 to 18)
* `target`: the target to which the indicator belings within its SDG. Targets are only defined for data obtained from the UN and the WDI since their indicators have been classified accordingly.
* `source`: the database from which the indicators were obtained (UN, WDI, WBP, WGI, GCI or OEC).
* `countryCode`: the 3-digit ISO code of the relevant country.
* `seriesCode`: The code of the indicator as it appears in its original database. This information can be used in the original documentation of the source.
* `seriesName`: The full description of the indicator, as provided by the original data.
* `instrumental`: A binary variable indicating whether we consider that the topic of the indicator is *instrumental*, *i.e.* that is has specific policy instruments and dedicated resources (see technical report for more details).
* `reverse`: A binary variable saying if the indicator needs to be reversed so that a higher value represents a better outcome. In the normalized data, all the indicators that required reversion have been reversed. In the raw data this is not the case.


## Sub-national Level Data


