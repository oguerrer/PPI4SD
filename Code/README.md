# Code for PPI

All the necessary functions to run PPI are in the file `ppi.py`, which is written in `Python 3`. We suggest installing the [Anaconda distribution](https://www.anaconda.com/distribution/) of Python. The folder `Examples` contains three examples on how use `ppi.py`. Here, we provide the documentation of its two functions: `run_ppi()` and `get_targets()`.




## run_ppi()
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


## get_targets()
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

