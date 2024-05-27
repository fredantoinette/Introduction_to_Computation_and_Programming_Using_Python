"""
Write a program that first stores the first ten numbers in the Fibonnaci 
sequence to a file named fib_file. Each number should be on a separate file in 
the file. The program should then read the numbers from the file and print 
them.
"""

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
    
with open('fib_file', 'w') as number_handle:
    for i in range(10):
        number_handle.write(str(fib(i)) + '\n')

with open('fib_file', 'r') as number_handle:
    for line in number_handle:
        print(line[:-1])
