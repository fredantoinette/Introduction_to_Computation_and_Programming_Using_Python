"""
Using the algorithm below, write a function that satisfies the specification

# Find lower bound on ans
lower_bound = 0
while 2**lower_bound < x:
    lower_bound += 1
low = lower_bound - 1
high = lower_bound + 1
# Perform bisection search
ans = (high + low) / 2
while abs(2**ans - x) >= epsilon:
    if 2**ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(ans, 'is close to the log base 2 of', x)

"""

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
    of x."""
    # Find lower bound on ans
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perform bisection search
    ans = (high + low) / 2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

print(log(4, 2, 0.01), 'is close to the log base 2 of', 4)
print(log(8, 2, 0.01), 'is close to the log base 2 of', 8)
print(log(9, 3, 0.01), 'is close to the log base 3 of', 9)
