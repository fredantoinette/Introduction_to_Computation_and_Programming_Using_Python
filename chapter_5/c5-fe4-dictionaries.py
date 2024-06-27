"""
Implement a function that meets the specification
"""

def get_min(d):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the alphabet.
    E.g., if d = {x = 11, b = 12}, get_min returns 12."""
    for key, val in d.items():
        if key == min(d):
            return val

d = {'x': 11, 'b': 12}
print(get_min(d))
d = {'b': 15, 'c': 16}
print(get_min(d))