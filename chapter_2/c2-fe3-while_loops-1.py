"""
Replace the comment in the following code with a while loop.

num_x = int(input('How many times should I print the letter X? '))
to_print = ''
#concatenate X to to_print num_x times
print(to_print)
"""

# option 1: using while loop
num_x = int(input('How many times should I print the letter X? '))
to_print = ''
while len(to_print) < num_x:
    to_print = to_print + 'X'
print(to_print)

# option 2: not using while loop
num_x = int(input('How many times should I print the letter X? '))
to_print = 'X' * num_x
print(to_print)
