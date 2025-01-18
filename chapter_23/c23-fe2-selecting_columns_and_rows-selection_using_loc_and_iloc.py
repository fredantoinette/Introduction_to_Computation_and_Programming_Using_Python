"""
Write an expression that selects all even numbered rows in wwc.
"""


import pandas as pd

wwc = pd.read_csv("wwc2019_q-f.csv")

print(wwc.loc[::2])
