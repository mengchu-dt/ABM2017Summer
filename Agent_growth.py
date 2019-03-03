#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 22:58:26 2017

@author: limengchu
"""

'''This module provides some population growth functions to generate a list of population 
   increment at each time period capturing the number of people enter the system at each stage. 
   NB: The output usually is not the whole population size at each time step. 

   An overview of the population growth models: 
   -------------------------------------------
    log_popgrow: Standard logistic growth model with the familiar S-shaped curve of growth. 
'''

import math

def log_popgrow(log_r = 0.001,log_K = 10**6 ,ini = 100, step = 50000):
    '''Parameters: 
       -----------------------------------
        log_r : float
                Malthusian parameter (growth rate)
        log_K : integer
                Carrying capacity (upper limit) in the logistic growth model
        ini   : integer
                initial population enter the model at period 1, should be positive
        step  : integer
                The estimated number of steps it takes from one person to the maximum capacity
                default is 50000.
    '''
    tau = step
    num_p = [0 for i in range(tau)]
    num_p[0] = 1
    for t in range(1,tau):
        log_p = sum(num_p[:t])  # number of people have entered the system 
        num_p[t] = int(math.ceil((log_r*log_p*(1-log_p/float(log_K)))))  # The increment of population size at time t
        if num_p[t] == 0: # when population stops increasing, we reach the capacity and exit the process
            br = t
            break
    p=num_p.index(ini) # find the initial value
    return num_p[p:br]


