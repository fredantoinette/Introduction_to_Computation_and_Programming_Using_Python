"""
Print a DataFrame containing only the games in which Sweden played either 
Germany or Netherlands.
"""


import pandas as pd

wwc = pd.read_csv("wwc2019_q-f.csv")
# print(wwc)

def get_country(df, country):
    """df a DataFrame with series labeled Winner and Loser
    country a str
    returns a DataFrame with all rows in which country appears
    in either the Winner or Loser column"""
    return df.loc[(df["Winner"] == country) | (df["Loser"] == country)]

def get_games(df, countries):
    return df[(df["Winner"].isin(countries)) | (df["Loser"].isin(countries))]

print(get_games(get_country(wwc, "Sweden"), ["Germany", "Netherlands"]))
