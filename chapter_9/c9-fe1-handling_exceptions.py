"""
Implement a function that meets the specification below. Use a try-except 
block. Hint: before starting to code, you might want to type something like 
1 + 'a' into the shell to see what kind of exception is raised.
"""

def sum_digits(s):
    """Asumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
    result = 0
    for i in s:
        try:
            result += int(i)
        except ValueError:
            result += 0
    return result
    
print(sum_digits('a2b3c'))
