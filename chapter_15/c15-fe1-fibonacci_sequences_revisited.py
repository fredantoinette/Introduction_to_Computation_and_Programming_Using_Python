"""
Use the tabular method to implement a dynamic programming solution that meets 
the specification
"""

def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, 
    change is a positive int,
    return the minimum number of coins needed to have a set of coins the values 
    which sum to change. Coins may be used more than once. For example, 
    make_change([1, 5, 8], 11) should return 3."""
    tab = [change + 1] * (change + 1)
    tab[0] = 0
    for i in range(1, change + 1):
        for val in coin_vals:
            if val <= change:
                temp = i // val + tab[i % val]
                if temp < tab[i]:
                    tab[i] = temp
    return tab[change]

print(make_change([1, 5, 8], 11)) # 3
print(make_change([1, 5, 10, 25, 50], 29)) # 5
print(make_change([1, 5, 10, 25], 87)) # 6
print(make_change([1, 3, 4, 5], 7)) # 2
