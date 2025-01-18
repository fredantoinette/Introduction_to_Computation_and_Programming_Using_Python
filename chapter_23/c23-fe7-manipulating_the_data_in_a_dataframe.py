"""
Write an expression that computes the total number of goals scored by the 
losing teams in the quarter finals.
"""


import pandas as pd

wwc = pd.read_csv("wwc2019_q-f.csv")
# print(wwc)

qf = wwc.loc[wwc["Round"] == "Quarters"]
# print(qf)

print(qf["L Goals"].sum())
