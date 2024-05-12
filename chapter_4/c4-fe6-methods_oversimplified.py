"""
Use find to implement a function satisfying the specification

"""

def find_last(s, sub):
    """s and sub are non-empty strings
        Returns the index of the last occurrence of sub in s.
        Returns None if sub does not occur in s"""
    if s.find(sub) == -1:
        return None
    else:
        start = 0
        while s.find(sub, start) != -1:
            str_position = s.find(sub, start)
            start = str_position + 1
        return str_position

print(find_last('testtest', 'test'))
print(find_last('testtesttesttesttesttest', 'test'))
print(find_last('testtesttest test testtest', 'test'))
print(find_last('testtest', 'python'))
print(find_last('testtest', 'TEST'))
