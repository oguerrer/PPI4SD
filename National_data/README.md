# Datasets

PPI4SD uses secondary data on development indicators, extracted from various sources.

## Splitting SDG 16
It should be noted that we have split SDG 16 in order to differentiate the topics of *peace and justice* and *strong institutions*. Thus, in this project, SDG 16a contains indicators of *peace and justice*, while SDG 16b covers *strong institutions*. This differentiation is important in the Mexican context, where governance issues may represent challenges that are not necessarily directly related to *peace and justice*.

## Development Indicators
The national level indicators consist of development indicators collected from various sources. Most of the data come from the United Nations Global SDG Database, which is the official source of the SDGs. However, in many cases, this source is insufficient to cover all the 17 SDGs. For this reason, we have complemented the official source with indicators from other databases and manually classified them into the SDGs, but not into targets.

These data cover the period 2006-2016, with each year coded into a column in a table. We provide two versions of these data: *normalized* and *raw*. In the normalized version, the indicators have been mapped into the interval [0,1], where zero and one are the lowest and highest values for that indicator (see the technical report for more details on this normalization). The raw version has the original values without normalization. Both datasets can be found in the CSV-formatted files: `final_sample_normalized.csv` and `final_sample_raw.csv`. The following table provides an example of the structure.

| 2005 | ... | 2017 | goal | target | countryCode | seriesCode | seriesName | instrumental | reverse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .552 | ... | .671 | 17 | 17.2 | MEX | 17.4.1_1 | Debt service as a proportion of exports of goods and services (%) | 1 | 1 |
| .043 | ... | .236 | 5 | NA | MEX | EOSQ088 | Ease of access to loans | 1 | 1 |

Example 1 provides a tutorial on how to load and visualize these data. Besides the columns representing the years of the observations, there are additional attributes that we explain bellow:

* `goal`: the SDG to which the indicator belongs (1 to 18)
* `target`: the target to which the indicator belongs within its SDG. Targets are only defined for data obtained from the UN and the WDI since their indicators have been classified accordingly.
* `countryCode`: the 3-digit ISO code of the relevant country.
* `seriesCode`: the code of the indicator as it appears in its original database. If there was no code assigned by the data supplier, then one was created (e.g. for most indicators in SDG 1).
* `seriesName`: the description of the indicator as provided by the original data.
* `instrumental`: a binary variable indicating whether we consider that the topic of the indicator is *instrumental*, *i.e.* that is has specific policy instruments and dedicated resources (see technical report for more details).
* `reverse`: a binary variable saying if the indicator needs to be reversed so that a higher value represents a better outcome. In the normalized data, all the indicators that required reversion have been reversed. In the raw data this is not the case.
* `seriesNameSpanish`: the description of the indicator in Spanish.
* `sourceName`: the name of the organization from which the indicators were obtained.
* `sourceNameSpanish`: the name in Spanish of the organization from which the indicators were obtained.
* `sourceProduct`: the name of the statistical product from which the data was obtained.
* `sourceProductSpanish`: the name in Spanish of the statistical product from which the data was obtained.
* `sourceLink`: the URL that provides access to the statistical product from which the indicator was obtained.
* `goalOfficial`: the official SDG of the indicator. The only difference with respect to `goal` is that `goalOfficial` does not split SDG 16, so all indicators in either SDG 16a or SDG 16b in `goal` appear as SDG 16 in `goalOfficial`.
* `goalColor`: the color of the corresponding SDG in hexadecimal format. A non-official color is assigned to SDG 16b to differentiate it from SDG 16a in the plots.
* `goalColorOfficial`: the official colors of the corresponding SDG in hexadecimal format.

## Network
The network of interdependencies between development indicators can be estimated by the user through various methods. [Ospina-Forero et al. (2019)](http://dx.doi.org/10.2139/ssrn.3385362) provide a comprehensive survey. For this project, we employ the method of Learning Sparse Bayesian Networks from High-Dimensional Data by [Aragam et al. (2017)](https://github.com/itsrainingdata/sparsebn). Here, we provide the file of the network that was estimated for this project. The file `network.csv` contains a squared matrix where each row and each column represents a development indicator. The rows and columns are ordered in the same fashion as in the files `final_sample_normalized.csv` and `final_sample_raw.csv`.

It should be noted that this network is not causal. Instead, it captures the conditional dependencies between the different development indicators. The direction of such dependencies goes from row to column. For example, if entry [3, 97] has a positive value, it means that the 3rd indicator conditions the change of the 97th indicator in a positive way. In other words, if we observe a change in the 97th indicator, we should expect that a change in the 3rd indicator took place in the same direction. Positive signs in this matrix represent synergies while negative ones correspond to trade-offs. Example 1 provides a tutorial to load and visualize these data.

## Growth Factors
To facilitate replicability, we provide the estimated growth factors (see methodological report). Since this estimation can be computationally intensive, we advise directly using the file `alphas.csv` to assign the values of each factor. If estimation is necessary, we also provide the code with the optimization heuristic.

The file `alphas.csv` contains a vector with the values of the growth factors. They are ordered in the same fashion as the files `final_sample_normalized.csv` and `final_sample_raw.csv`, so the first factor corresponds to the first indicator. Example 1 provides a tutorial on how to load and visualize these data.

## Development Goals
As explained in the methodological report, the development goals in a retrospective analysis are the final values of the development indicators. In a prospective analysis, the goals can be hypothetical values or data obtained from different sources. 

### Goals from the OECD Members
One way to think about development goals is in terms of a country emulating another. In terms of indicators, this would mean that a country could establish a set of goals based on the indicators of another country it wishes to emulate. In the technical report, we perform this exercise with the indicators of OECD members. File `goals_oecd.csv` contains each OECD country in a column, and provides the value of the indicator employed as goal in each row. The order of the rows corresponds to that of the files `final_sample_normalized.csv` and `final_sample_raw.csv`. Here we provide an example of these data:

| seriesCode | AUS_ini | AUT_ini | ... | GBR_fin | USA_fin |
| --- | --- | --- | --- | --- | --- |
| EOSQ035 | .873 | .871 | ... | .886 | .909 |
| LEGRGHTIDX | .785 | .736 | ... | .943 | .854 |

These data contains 34 OECD members others than Mexico. When a country's name as the suffix `_ini` it denotes the value of that indicator for that country in the initial period of the sample (2006). In contrast the suffix `_fin` indicates the value in the final period (2016). In addition to the OECD members, we also provide average indicator values (across countries) in the column `OECD_mean` and maximum values (across countries) in `OECD_max`.

### Goals from official Documents
An additional source of development goals for Mexico was obtained from the Annex XVIII-Bis of the [Mexican Parliamentary Gazette (2019)](http://gaceta.diputados.gob.mx/PDF/64/2019/abr/20190430-XVIII-1.pdf). This is a document produced by the Mexican Treasury, identifying multiple development indicators and establishing specific values as their goals. We provide these data after matching them to the main development indicators as explained in the technical report. File `goals_doc.csv` provides a vector with the goal for each indicator. The order of the rows corresponds to that of the files `final_sample_normalized.csv` and `final_sample_raw.csv`.

## SDG Budgeting


## References




