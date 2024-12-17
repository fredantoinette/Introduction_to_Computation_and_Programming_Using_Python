"""
Find the area between -1 and 1 for a standard normal distribution.
"""


import numpy as np
import scipy.integrate

def gaussian(x, mu, sigma):
    """assumes x, mu, sigma numbers
    returns the value of P(x) for a Gaussian
    with mean mu and sd sigma"""
    factor1 = (1.0 / (sigma * ((2 * np.pi)**0.5)))
    factor2 = np.e**-(((x - mu)**2 / (2 * sigma**2)))
    return factor1 * factor2

min_val = -1
max_val = 1
mu = 0
sigma = 1
print("The area between -1 and 1 under a Gaussian with mean of 0 and standard \
deviation of 1 is", 
str(round(scipy.integrate.quad(gaussian, min_val, max_val, (mu, sigma))[0], 5)))
