# ppi
Policy Priority Inference for Sustainable Development

Authors: Omar A. Guerrero & Gonzalo Castañeda
Written in Pyhton 3.7
Acknowledgments: This product was developed through the sponsorship of the
    United Nations Development Programme (bureau for Latin America)
    and with the support of the National Laboratory for Public Policies (Mexico City),
    the Centro de Investigación y Docencia Económica (CIDE, Mexico City),
    and The Alan Turing Institute (London).

This file contains all the necesary functions to reproduce the analysis presented
in the methodological and technical reports. The accompanying data can be
obtained from the public repository: https://github.com/oguerrer/PPI4SD.
There are two functions in this script:

    run_ppi : the main function that simulates the policymaking process and
    generates synthetic development-indicator data.
    get_targets : a support function to transform a collection of series
    where one or more targets are less or equals to the initial value of the series.

Further information can be found in each function's code.


Example
-------
To run PPI in a Python script, just add the following line:

    tsI, tsC, tsF, tsP, tsD, tsS, ticks, H = run_ppi(I0, T)

This will simulate the policymaking process for initial values I0 and targets T.
This example assumes no network of spillovers. All other arguments can be
passed as explained in the function run_ppi.


Rquired external libraries
--------------------------
- Numpy



## run_ppi
```python
run_ppi(I0, T, A=None, alpha=0.1, phi=0.5, tau=0.5, R=None, gov_func=None, P0=None, H0=None, PF=None, pf=1, tolerance=0.001)
```
Function to run one simulation of the Policy Priority Inference model.

Parameters
----------
    I0: numpy array
        Initial values of the development indicators.
    T: numpy array
        Target values for development indicators. These values represent
        the government's goals or aspirations. For a retrospective analysis,
        it is usually assumed that the targets correspond to the final values
        of the series. They should be higher than I0 or the model will not
        converge.
    A:  2D numpy array
        The adjacency matrix of the spillover network of development
        indicators. If not given, the model assumes a zero-matrix, so there
        are no spillovers.
    alpha: float, optional
        A vector of growth factors in (0,1).
    phi: float, optional
        Scalar in [0,1] or numpy array (a vector) with values in [0,1] that
        represent the quality of the government's monitoring mechanisms.
    tau: float, optional
        Scalar in [0,1] or numpy array (a vector) with values in [0,1] that
        represent the quality of the rule of law.
    R: numpy array, optional
        Binary vector indicating which nodes are instrumental (value 1) and
        which are not (value 0). If not provided, it is assumed that all
        nodes are instrumental (a vector of ones).
    gov_func: python function, optional
        A custom function that that returns the policy priority of the governemnt
    P0: numpy array, optional
        An array with the initial allocation profile.
    H0: numpy array, optional
        The initial vector of historical inefficiencies
    PF: numpy array, optional
        An exogenous vector of policy priorities.
    pf: float, optional
        The probability with which the exogenous priorities are followed
        each period. It must be in [0,1].
    tolerance: float, optional
        The precision to consider that an indicator has reached its goal.
        Unless you understand very well how PPI works, this should not be
        changed.

Returns
-------
    tsI: 2D numpy array
        Matrix with the time series of the simulated indicators. Each column
        corresponds to a simulation step.
    tsC: 2D numpy array
        Matrix with the time series of the simulated contributions. Each column
        corresponds to a simulation step.
    tsF: 2D numpy array
        Matrix with the time series of the simulated agents' benefits. Each column
        corresponds to a simulation step.
    tsP: 2D numpy array
        Matrix with the time series of the simulated resource allocations.
        Each column corresponds to a simulation step.
    tsD: 2D numpy array
        Matrix with the time series of the simulated inefficiencies. Each column
        corresponds to a simulation step.
    tsS: 2D numpy array
        Matrix with the time series of the simulated spillovers. Each column
        corresponds to a simulation step.
    ticks: numpy array
        A vector with the simulation step in which each indicator reached its target.
    H: numpy array
        A vector with historical inefficiencies,

## get_targets
```python
get_targets(series)
```
Transforms a collection of series where one or more targets are less or
equals to the initial value of the series.

Parameters
----------
    series: numpy 2D array
        A matrix containing the time series of each indicator. Each row
        corresponds to a series and each column to a period.

Returns
-------
    I0: numpy array
        The initial values of each series.
    T: numpy array
        The transformed targets (final values) of each series.

