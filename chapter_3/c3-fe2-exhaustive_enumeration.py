"""
Write a program that asks the user to enter an integer and prints two integers,
root and pwr, such that 1 < pwr < 6 and root**pwr is equal to the integer 
entered by the user. If no such pair of integers exists, it should print a 
message to that effect.
"""

root = 0
pwr = 0
x = int(input('Enter an integer: '))
for r in range(x + 1):
    for p in range(2, 6):
        if r**p == x:
            root = r
            pwr = p
            break
if root == 0 and pwr == 0:
    print('There is no pair of root and pwr')
else:
    print('root =', root, ';', 'pwr =', pwr)