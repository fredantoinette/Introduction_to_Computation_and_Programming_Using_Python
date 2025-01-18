"""
Find the coefficient of determination (r^2) for the mean annual temperature 
rather than for the rolling average and for a ten-year rolling average.
"""


import pandas as pd
import numpy as np


# Building a dictionary mapping years to temperature data

def get_dict(temperatures, labels):
    """temperatures a DataFrame. Its indices are ints
    representing dates of the form yyyymmdd
    labels a list of column labels
    returns a dict with strs representing years as keys,
    the values dicts with the columns as keys, and
    a list of the daily temperatures in that column for
    that year as values
    """
    year_dict = {}
    for index, row in temperatures.iterrows():
        year = str(index)[0:4]
        try:
            for col in labels:
                year_dict[year][col].append(row[col])
        except:
            year_dict[year] = {col:[] for col in labels}
            for col in labels:
                year_dict[year][col].append(row[col])
    return year_dict


# Building a DataFrame organised around years

temperatures = pd.read_csv("US_temperatures.csv")
temperatures.set_index("Date", drop = True, inplace = True)
temperatures["Mean T"] = round(temperatures.mean(axis = "columns"), 2)
temperatures["Max T"] = temperatures.max(axis = "columns")
temperatures["Min T"] = temperatures.min(axis = "columns")
yearly_dict = get_dict(temperatures, ["Max T", "Min T", "Mean T"])
years, mins, maxes, means = [], [], [], []
for y in yearly_dict:
    years.append(y)
    mins.append(min(yearly_dict[y]["Min T"]))
    maxes.append(max(yearly_dict[y]["Max T"]))
    means.append(round(np.mean(yearly_dict[y]["Mean T"]), 2))
    
yearly_temps = pd.DataFrame({"Year": years, "Min T": mins,
                             "Max T": maxes, "Mean T": means})


def r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
    predicted a one-dimensional array of predicted values
    Returns coefficient of determination"""
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum() / len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error / variability

yearly_temps["Year"] = yearly_temps["Year"].apply(int)

model = np.polyfit(list(yearly_temps["Year"]), 
                   list(yearly_temps["Mean T"]), 1)
# r^2 for mean annual temperature
print(r_squared(yearly_temps["Mean T"], 
                np.polyval(model, yearly_temps["Year"])))

num_years = 10
for label in ["Min T", "Max T", "Mean T"]:
    yearly_temps[label] = yearly_temps[label].rolling(num_years).mean()

indices = np.isfinite(yearly_temps["Mean T"])
model = np.polyfit(list(yearly_temps["Year"][indices]), 
                   list(yearly_temps["Mean T"][indices]), 1)
# r^2 for ten-year rolling average
print(r_squared(yearly_temps["Mean T"][indices], 
                np.polyval(model, yearly_temps["Year"][indices])))
