"""
Write an expression that evaluates to the mean of a tuple of numbers. Use the 
function sum.
"""

def mean_tuple(*numbers):
    total = sum(numbers)
    count = 0
    for elem in numbers:
        count += 1
    return total / count

# test
print(mean_tuple(1, 3, 6, 8))
print(mean_tuple(0,))
print(mean_tuple(-5, 5, 9))