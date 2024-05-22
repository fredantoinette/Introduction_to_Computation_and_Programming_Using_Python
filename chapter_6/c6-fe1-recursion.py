"""
The harmonic sum of an integer, n > 0, can be calculated using the formula 
1 + 1/2 + ... + 1/n. Write a recursive function that computes this.
"""

def harmonic_sum(n):
    if n == 1:
        return n
    else:
        return 1/n + harmonic_sum(n - 1)
    
# test
print(harmonic_sum(1))
print(harmonic_sum(3))
#print(1 + 1/2 + 1/3)
print(harmonic_sum(6))
#print(1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6)
print(harmonic_sum(10))
#print(1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/9 + 1/10)
