"""
Write a list comprehension that generates all non-primes between 2 and 100.
"""

print([x for x in range(2, 100) if not all(x % y != 0 for y in range(2, x))])


# equivalent function
def gen_non_primes():
    non_primes = []
    for x in range(2, 100):
        not_prime = False
        for y in range(2, x):
            if x % y == 0:
                not_prime = True
        if not_prime:
            non_primes.append(x)
    return non_primes
print(gen_non_primes())
