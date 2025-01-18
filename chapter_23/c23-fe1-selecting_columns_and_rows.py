"""
Write a function that returns the sum of the goals scored by winners.
"""


import pandas as pd

wwc = pd.read_csv("wwc2019_q-f.csv")

sum_goals_w = 0 
for g in wwc["W Goals"]:
    sum_goals_w += g
print(sum_goals_w)
