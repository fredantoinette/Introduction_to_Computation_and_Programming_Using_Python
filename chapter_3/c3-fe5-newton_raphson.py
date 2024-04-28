"""
Add some code to the implementation of Newton-Raphson that keeps track of the 
number of iterations used to find the root. Use that code as part of a program 
that compares the efficiency of Newton-Raphson and bisection search. (You 
should discover that Newton-Raphson is far more efficient.)

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0.01
epsilon = 0.01
guess = k / 2
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
print('Square root of', k, 'is about', guess)

"""

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0.01
k = 24
epsilon = 0.01
guess = k / 2
num_iterations = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
    #print('guess =', guess)
    num_iterations += 1
print('Newton-Raphson')
print('Square root of', k, 'is about', guess)
print('Number of iterations =', num_iterations)
print('----------')

# Bisection search for square root
num_iterations = 0 # reset
low = 0
high = max(1, k)
guess = (high + low) / 2
while abs(guess**2 - k) >= epsilon:
    #print('low =', low, 'high =', high, 'guess =', guess)
    num_iterations += 1
    if guess**2 < k:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
print('Bisection Search')
print('Square root of', k, 'is about', guess)
print('Number of iterations =', num_iterations)
