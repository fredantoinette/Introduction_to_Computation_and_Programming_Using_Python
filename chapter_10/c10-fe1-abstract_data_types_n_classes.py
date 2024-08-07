'''
Add a method satisfying the specification below to the Int_set class.

def union(self, other):
    """other is an Int_set
    mutates self so that it contains exactly the
    elements in self
    plus the elements in other."""
    
'''

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

    def union(self, other):
        """other is an Int_set
        mutates self so that it contains exactly the
        elements in self
        plus the elements in other."""
        for i in other:
            if i not in self._vals:
                self._vals.append(i)


# test
s = Int_set()
s.insert(3)
s.insert(4)
print('The value of s is', s)
s.union({9, 6, 3})
print('The value of s is', s)
