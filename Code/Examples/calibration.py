# -*- coding: utf-8 -*-
"""Policy Priority Inference for Sustainable Development - Estimation & Calibration Code

Authors: Omar A. Guerrero & Gonzalo Castañeda
Written in Pyhton 3.7
Acknowledgments: This product was developed through the sponsorship of the
    United Nations Development Programme (bureau for Latin America) 
    and with the support of the National Laboratory for Public Policies (Mexico City), 
    the Centro de Investigación y Docencia Económica (CIDE, Mexico City), 
    and The Alan Turing Institute (London).

This file contains all the necesary functions to estimate the growth factors
of the model and to calibrate the number of periods for convergence. The accompanying 
data can be obtained from the public repository: https://github.com/oguerrer/PPI4SD. 
The two main functions are:
    
    calibrate: finds the optimal number of periods for convergence in terms of 
                matching the total volatility of the indicators' changes
    estimation: given the number of periods for convergence, this function
                estimates the growth factors of the model

There are additional support functions that are explained below.


Example
-------
To run PPI in a Python script, just add the following line:

    steps, alphas = estimation(I0, T, A, R, phi, tau, vola_emp, steps, initial_alphas)
    
This returns the growth factors in the vector 'alphas'.


Rquired external libraries
--------------------------
- Numpy
- Scipy
- joblib: the joblib library takes care of the parallel processing. It installation
            is straightforward and the instructions can be found in its
            Pypi site: https://pypi.org/project/joblib/

"""

# import necessary libraries
from __future__ import division, print_function
import numpy as np
import copy
from joblib import Parallel, delayed
import scipy.optimize as opt

# the model_final.py file should be in the same folder
from model_final import * 



def run_model(I0, T, A, R, phi, tau, alphas, sampleSize):
    """Runs the model for a given number of times and returns a matrix with the
    convergence times of each indicator in each simulation.

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
        R: numpy array, optional
            Binary vector indicating which nodes are instrumental (value 1) and 
            which are not (value 0). If not provided, it is assumed that all
            nodes are instrumental (a vector of ones).
        phi: float, optional
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the government's monitoring mechanisms.
        tau: float, optional 
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the rule of law.
        alphas: numpy array 
            A vector with the growth factors. Each element shuold be in (0,1).
        sampleSize: int 
            The number of simulations to be performed.
        
    Returns
    -------
        all_times: numpy array
            A matrix with the convergence times of each indicator in each 
            simulation. The rows correspond to the indicators and the columns
            to the simulations.
    """
    all_times = []
    for intera in range(sampleSize):
        outputs = run_ppi(I0, T, A=A, alpha=alphas, R=R, phi=phi, tau=tau, tolerance=1e-3)
        tsI, tsC, tsF, tsP, tsD, tsS, times, H = outputs
        all_times.append(times)
    all_times = np.array(all_times).T
    return all_times
        
        
def fobj(alpha, node, alphaStar, steps, sampleSize, I0, T, A, R, phi, tau):
    """A wrapper around the 'run_model' function that will be used to perform
    the greedy search.

    Parameters
    ----------
        alpha: float
            The value of the growth factor to be changed. Shuold be in (0,1).
        node: int
            The index (from 0 to N-1) of the node to which the growth factor
            'alpha' corresponds.
        alphaStar: numpy array 
            A vector with the growth factors. Each element shuold be in (0,1).
        steps: int
            Number of steps to which the simulation should converge. It is used
            to evaluate convergence time errors.
        sampleSize: integer 
            The number of simulations to be performed.
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
        R: numpy array, optional
            Binary vector indicating which nodes are instrumental (value 1) and 
            which are not (value 0). If not provided, it is assumed that all
            nodes are instrumental (a vector of ones).
        phi: float, optional
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the government's monitoring mechanisms.
        tau: float, optional 
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the rule of law.
        
        
    Returns
    -------
        errors: numpy array
            The squared differences between 'steps' and the convergence time of
            each indicator.
    """
    alphas = copy.deepcopy(alphaStar)
    alphas[node] = alpha
    all_times = run_model(I0, T, A, R, phi, tau, alphas, sampleSize)
    errors = (all_times.mean(axis=1)[node] - steps)**2
    return errors


def func(I0, T, A, R, phi, tau, node, alphas, steps, sampleSize):
    """Greedy search of a growth factor for indicator 'node' that minimizes
    the difference between its convergence time and 'steps'.

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
        R: numpy array, optional
            Binary vector indicating which nodes are instrumental (value 1) and 
            which are not (value 0). If not provided, it is assumed that all
            nodes are instrumental (a vector of ones).
        phi: float, optional
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the government's monitoring mechanisms.
        tau: float, optional 
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the rule of law.
        node: int
            The index (from 0 to N-1) of the node to which the searched 
            growth factor corresponds.
        alphas: numpy array 
            A vector with the growth factors. Each element shuold be in (0,1).
        steps: int
            Number of steps to which the simulation should converge. It is used
            to evaluate convergence time errors.
        sampleSize: integer 
            The number of simulations to be performed.
        
    Returns
    -------
        best_alpha: float
            The growth factor that minimizes the difference between the convergence
            time of 'node' and 'steps', keeping everything else constant.
    """
    sol = opt.minimize_scalar(fobj, args=(node, alphas, steps, sampleSize, I0, T, A, R, phi, tau), bounds=[.01, .99], method='Bounded')
    best_alpha = sol.x
    return best_alpha


def aver_dev(mean_times, steps):
    """Computes the average mean difference between the average convergence times
    and 'steps'.

    Parameters
    ----------
        mean_times: numpy array 
            A vector with the mean convergence time of each indicator.
        steps: integer 
            Number of steps to which the simulation should converge.
        
    Returns
    -------
        aver_error: float
            The average difference between the mean convergence times and 'steps'.
    """
    aver_error = np.mean(np.abs(mean_times - steps))
    return aver_error


def estimate(I0, T, A, R, phi, tau, vola_emp,
               steps, parallel_processes=4, sample_size=1000, alphas=None, 
               dev_lim=.8):
    """Estimates the growth factors for a given number of periods to convergence.

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
        R: numpy array, optional
            Binary vector indicating which nodes are instrumental (value 1) and 
            which are not (value 0). If not provided, it is assumed that all
            nodes are instrumental (a vector of ones).
        phi: float, optional
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the government's monitoring mechanisms.
        tau: float, optional 
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the rule of law.
        vola_emp: float
            The total standard deviation of the changes of the empirical
            indicators.
        steps: int
            Number of steps to which the simulation should converge. It is used
            to evaluate convergence time errors.
        parallel_processes: float, optional
            Number of processes to be ran in parallel.
        sample_size: int, optional
            The number of simulations to be ran for each estimation.
        alphas: numpy array, optional
            Initial values for the growth factors.
        dev_lim: float, optional
            Tolerance threshold for the difference between the mean convergence 
            times and 'calib_steps'.
        
    Returns
    -------
    alphas: list
            A list with numpy arrays. Each array contains the growth factors 
            estimated for each 'calib_steps'.
    vola_sim: list
            A list with the different 'steps' iterated in the function.
    
    """
    N = len(R)
    if alphas is  None:
        est_alphas = np.ones(N)*.5
    else:
        est_alphas = copy.deepcopy(alphas)
    
    all_times = run_model(I0, T, A, R, phi, tau, est_alphas, sample_size)
    mean_devs = aver_dev(all_times.mean(axis=1), steps)
    keep_looking = True
    while keep_looking:
        print('Number of ticks to convergence:', steps)
        print('Mean convergence time error:', mean_devs)
        above_std = np.where(np.abs(all_times.mean(axis=1)-steps) > dev_lim)[0]
        sol = Parallel(n_jobs=parallel_processes, verbose=0)(delayed(func)(I0, T, A, R, phi, tau, 
                       node, est_alphas, steps, sample_size) for node in above_std)
        est_alphas[above_std] = sol
        all_times = run_model(I0, T, A, R, phi, tau, est_alphas, sample_size)
        mean_devs = aver_dev(all_times.mean(axis=1), steps)
        
        if mean_devs < dev_lim:
            keep_looking = False
            out_times = []
            all_tsI = []
            for intera in range(sample_size):
                outputs = run_ppi(I0, T, A=A, alpha=est_alphas, R=R, phi=phi, tau=tau)
                tsI, tsC, tsF, tsP, tsD, times, tsS, H = outputs
                out_times.append(times)
                all_tsI.append(tsI)

            nchs_sim_dist = []
            for ts in all_tsI:
                chs_sim = ts[:,1:]-ts[:,0:-1]
                nchs_sim_dist += chs_sim.flatten().tolist()
            est_vola = np.std(nchs_sim_dist)
                
    return est_alphas, est_vola


def find_steps(I0, T, A, R, phi, tau, vola_emp, alphas=None,
              parallel_processes=4, sample_size=10, dev_lim=3, steps=10):
    """Iterates over the number of 'steps' to convergence until the total volatility
    of the synthetic indicators is lower than the empirical one.

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
        R: numpy array, optional
            Binary vector indicating which nodes are instrumental (value 1) and 
            which are not (value 0). If not provided, it is assumed that all
            nodes are instrumental (a vector of ones).
        phi: float, optional
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the government's monitoring mechanisms.
        tau: float, optional 
            Scalar in [0,1] or numpy array (a vector) with values in [0,1] that 
            represent the quality of the rule of law.
        vola_emp: float
            The total standard deviation of the changes of the empirical
            indicators.
        parallel_processes: float, optional
            Number of processes to be ran in parallel.
        sample_size: int, optional
            The number of simulations to be ran for each estimation.
        dev_lim: float, optional
            Tolerance threshold for the difference between the mean convergence 
            times and 'calib_steps'.
        steps: int, optional
            The minimum number of simulation steps for convergence.
        
    Returns
    -------
    rec_alphas: list
            A list with numpy arrays. Each array contains the growth factors 
            estimated for each 'calib_steps'.
    rec_volas: list
            A list with with the total standard deviation of the simulated 
            indicators. Each standard deviation corresponds to each 'calib_steps'.
    rec_steps: list
            A list with the different 'calib_steps' iterated in the function.
    """
    N = len(R)
    if alphas is  None:
        alphas = np.ones(N)*.5
    else:
        est_alphas = copy.deepcopy(alphas)
    cont_T = True
    
    rec_alphas = []
    rec_volas = []
    rec_steps = []
    
    while cont_T:
        
        est_alphas, est_vola = estimate(I0=I0, T=T, A=A, R=R, phi=phi, tau=tau,
                                           vola_emp=vola_emp, steps=steps,
                                           parallel_processes=parallel_processes,
                                           sample_size=sample_size, alphas=alphas, 
                                           dev_lim=dev_lim,)
                
        rec_alphas.append(est_alphas)
        rec_volas.append(est_vola)
        rec_steps.append(steps)
        steps += 1
                
        print('Difference in volatility:', est_vola - vola_emp)
        
        if est_vola < vola_emp:
            cont_T = False
            
            
    return rec_alphas, rec_volas, rec_steps







































