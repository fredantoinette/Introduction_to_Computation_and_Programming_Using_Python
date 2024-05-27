"""
Since 1958, Canadian Thanksgiving has occurred on the second Monday in October. 
Write a function that takes a year (>1957) as a parameter, and returns the 
number of days between Canadian Thanksgiving and Christmas.
"""

import calendar as cal

def num_days(year):
    tg_month = cal.monthcalendar(year, 10)
    if tg_month[0][cal.MONDAY] != 0:
        tg_day = tg_month[1][cal.MONDAY]
    else:
        tg_day = tg_month[2][cal.MONDAY]
    last_day_oct = max(max(cal.monthcalendar(year, 10)))
    days_oct = last_day_oct - tg_day
    days_nov = max(max(cal.monthcalendar(year, 11)))
    days_dec = 24
    return days_oct + days_nov + days_dec # exclude Thanksgiving & Christmas days

print('Number of days between Canadian Thanksgiving and Christmas in 2023 is', num_days(2023))
print('Number of days between Canadian Thanksgiving and Christmas in 2024 is', num_days(2024))
print('Number of days between Canadian Thanksgiving and Christmas in 2025 is', num_days(2025))
