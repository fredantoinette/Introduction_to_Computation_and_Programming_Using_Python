'''
def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
'''
"""
When the implementation of fib above is used to compute fib(5), how many times 
does it compute the value of fib(2) on the way to computing fib(5)?
"""

list_fib = []

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        list_fib.append('fib' + str(n-1))
        list_fib.append('fib' + str(n-2))
        #print(f'fib{n-1} + fib{n-2}')
        return fib(n-1) + fib(n - 2)

print(fib(5))
#print(list_fib)
print(list_fib.count('fib2'))
