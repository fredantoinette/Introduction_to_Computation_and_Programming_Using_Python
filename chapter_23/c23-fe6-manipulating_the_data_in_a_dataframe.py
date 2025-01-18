"""
Write an expression that computes the total number of goals scored in all of 
the rounds.
"""


import pandas as pd

wwc = pd.read_csv("wwc2019_q-f.csv")
# print(wwc)

print(wwc["W Goals"].sum() + wwc["L Goals"].sum())
