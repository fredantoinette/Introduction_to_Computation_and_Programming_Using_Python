"""
Use the find_root function below to print the sum of approximations to the 
square root of 25, the cube root of -8, and the fourth root of 16. Use 0.001 
as epsilon.

def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power % 2 == 0:
        return None # Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

"""

def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power % 2 == 0:
        return None # Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

epsilon = 0.001
a = find_root(25, 2, epsilon)
b = find_root(-8, 3, epsilon)
c = find_root(16, 4, epsilon)
print(f'sum of approximations = {a} + {b} + {c} = {a + b + c}')
