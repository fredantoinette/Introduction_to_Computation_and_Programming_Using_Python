"""
Write code to extract the date on which the temperature in Phoenix was 41.4C.
"""


import pandas as pd

temperatures = pd.read_csv("US_temperatures.csv")

# print(temperatures.loc[temperatures["Phoenix"] == 41.4][["Date", "Phoenix"]])
print(temperatures.loc[temperatures["Phoenix"] == 41.4]["Date"])
