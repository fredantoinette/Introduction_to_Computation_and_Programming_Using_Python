"""
Replace the union method you added to Int_set by a method that allows clients 
of Int_set to use the + operator to denote set union.
"""

class Int_set(object):
    """An Int_set is a set of integers"""
    #Information about the implementation (not the abstraction):
        #Value of a set is represented by a list of ints, self._vals.
        #Each int in a set occurs in self._vals exactly once.
        
    def __init__(self):
        """Create an empty set of integers"""
        self._vals = []
        
    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)
            
    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self._vals
    
    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self._vals.remove()
        except:
            raise ValueError(str(e) + ' not found')
    
    def get_members(self):
        """Returns a list containing the elements of self._
        Nothing can be assumed about the order of the elements"""
        return self._vals[:]
    
    def __str__(self):
        """Returns a string representation of self"""
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'

    def __add__(self, other):
        new_set = Int_set()
        for i in self._vals:
            if i not in new_set._vals:
                new_set._vals.append(i)
        for j in other._vals:
            if j not in new_set._vals:
                new_set._vals.append(j)
        return new_set


# test
s1 = Int_set()
s2 = Int_set()
s1.insert(3)
s1.insert(4)
s2.insert(6)
s2.insert(3)
print('The value of s1 is', s1)
print('The value of s2 is', s2)
s3 = s1 + s2
print('The value of s3 is', s3)
