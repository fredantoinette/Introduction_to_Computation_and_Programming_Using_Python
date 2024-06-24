"""
Write a program that asks the user to input 10 integers,
and then prints the largest odd number that was entered.
If no odd number was entered,
it should print a message to that effect.
"""

odd_int = 0
num_iterations = 0
while num_iterations < 10:
    user_int = input(f'Please input an integer ({num_iterations+1}): ')
    if int(user_int) % 2 != 0: 
        if odd_int == 0:
            odd_int = int(user_int)
        elif int(user_int) > odd_int:
            odd_int = int(user_int)
    num_iterations = num_iterations + 1
if odd_int != 0:
    print(f'The largest odd number is {odd_int}')
else:
    print("No odd number was entered")
