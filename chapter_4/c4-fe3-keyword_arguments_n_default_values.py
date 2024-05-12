"""
Write a function mult that accepts either one or two ints as arguments. If 
called with two arguments, the function prints the products of the two 
arguments. If called with one argument, it prints that argument.
"""

def mult(int1 = 1, int2 = 1):
    print(int1 * int2)
        
# test    
mult(int1 = 2, int2 = 3)
mult(int1 = 3, int2 = 2)
mult(2, 3)
mult(int1 = 5)
mult(int2 = 5)
mult(5)
