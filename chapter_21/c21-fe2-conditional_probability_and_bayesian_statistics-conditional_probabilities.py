"""
Estimate the probability that a randomly chosen American is both male and 
weighs more than 197 pounds. Assume that 50% of the population is male, and 
that the weights of the male population are normally distributed with a mean of 
210 pounds and a standard deviation of 30 pounds. (Hint: think about using the 
empirical rule.)
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

# P(weight > 197 and male) = P(male) * P(weight < 197 | male)
min_val = 0
max_val = 197
mu = 210
sigma = 30
# B = male
prob_b = 0.5 # probability of being male
# A = weight > 197
# not A = weight <= 197
prob_not_a_given_b = scipy.integrate.quad(gaussian, min_val, max_val, (mu, sigma))[0] # probability of weighing <= 197 pounds, given that the person is a male
prob_a_given_b = 1 - prob_not_a_given_b # probability of weighing > 197 pounds, given that the person is a male
prob_a_n_b = prob_a_given_b * prob_b # probability of weighing > 197 pounds & being male
print(prob_a_n_b)
