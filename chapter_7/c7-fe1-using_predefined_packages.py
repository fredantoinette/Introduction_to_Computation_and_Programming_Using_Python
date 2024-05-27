'''
Write a function that meets the specification

def shopping_days(year):
    """year a number >= 1941
    returns the number of days between U.S. Thanksgiving and
    Christmas in year"""
    
'''

import calendar as cal

def shopping_days(year):
    """year a number >= 1941
    returns the number of days between U.S. Thanksgiving and
    Christmas in year"""
    tg_month = cal.monthcalendar(year, 11)
    if tg_month[0][cal.THURSDAY] != 0:
        tg_day = tg_month[3][cal.THURSDAY]
    else:
        tg_day = tg_month[4][cal.THURSDAY]
    last_day_nov = max(max(cal.monthcalendar(year, 11)))
    days_nov = last_day_nov - tg_day
    days_dec = 24
    return days_nov + days_dec # exclude Thanksgiving & Christmas days

print('Number of days between U.S. Thanksgiving and Christmas in 2023 is', shopping_days(2023))
print('Number of days between U.S. Thanksgiving and Christmas in 2024 is', shopping_days(2024))
print('Number of days between U.S. Thanksgiving and Christmas in 2025 is', shopping_days(2025))
print('Number of days between U.S. Thanksgiving and Christmas in 2026 is', shopping_days(2026))
print('Number of days between U.S. Thanksgiving and Christmas in 2015 is', shopping_days(2015))
