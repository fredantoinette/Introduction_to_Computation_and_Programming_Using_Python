"""
Write a program that examines three variables--x, y, and z--and prints the largest odd number among them.
If none of them are odd, it should print the smallest value of the three.
"""

def largest_odd_or_smallest_value(x, y, z):
    answer = min(x, y, z)
    if x % 2 != 0:
        answer = x
    if y % 2 != 0 and y > answer:
        answer = y
    if z % 2 != 0 and z > answer:
        answer = z
    print(answer)
    
# test    
largest_odd_or_smallest_value(3, 5, 7)
largest_odd_or_smallest_value(2, 8, 4)
largest_odd_or_smallest_value(9, 5, 12)
largest_odd_or_smallest_value(3, 6, 10)
