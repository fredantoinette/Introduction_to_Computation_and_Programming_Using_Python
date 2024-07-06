"""
Implement a function that satisfies the specification
"""

def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    for e in L:
        if e % 2 == 0:
                return e
    raise ValueError("L does not contain an even number")

# test
print(find_an_even([2, 3, 4]))
print(find_an_even([3, 4, 5]))
print(find_an_even([5, 7, 9]))
