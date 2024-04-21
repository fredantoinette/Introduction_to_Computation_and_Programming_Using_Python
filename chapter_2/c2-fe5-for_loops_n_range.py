"""
Write a program that prints the sum of the prime numbers greater than 2 and less than 1000.
Hint: you probably want to use a for loop that is a primality test nested inside 
a for loop that iterates over the odd integers between 3 and 999.
"""

sum_prime_num = 0
for i in range(3, 1000, 2):
    is_prime = True
    for j in range (3, i, 2):
        if i != j and i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        sum_prime_num = sum_prime_num + i
print(sum_prime_num)
