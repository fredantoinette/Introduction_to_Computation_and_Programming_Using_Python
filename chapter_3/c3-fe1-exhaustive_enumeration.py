"""
Change the code below so that it returns the largest rather than the smallest 
divisor. Hint: if y*z = x and y is the smallest divisor of x, z is the largest 
divisor of x.

# Test if an int > 2 is prime. If not, print smallest divisor
x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')
    
"""

# Test if an int > 2 is prime. If not, print largest divisor
x = int(input('Enter an integer greater than 2: '))
largest_divisor = None
for guess in range(2, x):
    if x % guess == 0:
        largest_divisor = x / guess
        break
if largest_divisor != None:
    print('Largest divisor of', x, 'is', largest_divisor)
else:
    print(x, 'is a prime number')
