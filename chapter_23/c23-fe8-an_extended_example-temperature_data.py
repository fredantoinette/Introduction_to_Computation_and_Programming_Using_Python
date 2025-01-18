"""
Write an expression that evaluates to True if Phoenix was warmer than Tampa on 
October 31, 2000, and False otherwise.
"""


import pandas as pd

temperatures = pd.read_csv("US_temperatures.csv")

p_temp = temperatures.loc[temperatures["Date"] == 20001031]["Phoenix"]
# print(p_temp)
t_temp = temperatures.loc[temperatures["Date"] == 20001031]["Tampa"]
# print(t_temp)
print(p_temp > t_temp)
