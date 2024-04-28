"""
What would have to be changed to make the following code work for finding an 
approximation to the cube root of both negative and positive numbers?
Hint: think about changing low to ensure that the answer lies within the 
region being searched.

epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)

"""

# x = -25 # try negative integer
# x = 25 # try positive integer
# x = 0.25 # try positive decimal
x = -0.25 # try negative decimal

epsilon = 0.0001 # improving accuracy
num_guesses = 0
low = min(-1, x) # -1 so can handle -1 < x < 0
high = max(1, x) # 1 so can handle 0 < x < 1
ans = (high + low) / 2
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print('number of guesses =', num_guesses)
print(ans, 'is close to cube root of', x)
