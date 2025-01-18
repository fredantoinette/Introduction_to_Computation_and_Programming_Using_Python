"""
Write an expression that generates the DataFrame
"""


import pandas as pd

wwc = pd.read_csv("wwc2019_q-f.csv")

print(wwc.loc[1:2])
