'''
Add to Grades a generator that meets the specification

def get_students_above(self, grade):
    """Return the students a mean grade > g one at a time"""
    
'''

import datetime


class Person(object):
    
    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1 :]
        except:
            self._last_name = name
        self._birthday = None
        
    def get_name(self):
        """Returns self's full name"""
        return self._name
        
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
        
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self._birthday = birthdate
            
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
        
    def __lt__(self, other):
        """Assumes other a Person
        Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
        
    def __str__(self):
        """Returns self's name"""
        return self._name


class MIT_person(Person):
    
    _next_id_num = 0 #identification number
    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num
    
    def is_student(self):
        return isinstance(self, Student)
    
    '''
    def is_student(self):
        return type(self) == Grad or type(self) == UG
    '''
    
    
class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    def get_class(self):
        return self._year

class Grad(Student):
    pass

class Transfer_student(Student):
    def __init__(self, name, from_school):
        MIT_person.__init__(self, name)
        self._from_school = from_school
    def get_old_school(self):
        return self._from_school
    
    
class Grades(object):
    
    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True
        
    def add_student(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False
        
    def add_grade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')
            
    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')
            
    def get_students(self):
        """Return the students in the grade book one at a time
        in alphabetical order"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s
            
    def get_students_above(self, grade):
        """Return the students a mean grade > g one at a time"""
        for s in self.get_students():
            total_grades = 0
            num_grades = 0
            for g in self.get_grades(s):
                total_grades += g
                num_grades += 1
            mean = total_grades / num_grades
            if mean > grade:
                yield s
            

# test             
grades = Grades()
grad1 = Grad('A')
grad2 = Grad('B')
grad3 = Grad('C')
grades.add_student(grad1)
grades.add_student(grad2)
grades.add_student(grad3)
for s in grades.get_students():
    grades.add_grade(s, 75)
grades.add_grade(grad1, 25)
grades.add_grade(grad2, 50)
grades.add_grade(grad3, 100)
print(grades.get_grades(grad1))
print(grades.get_grades(grad2))
print(grades.get_grades(grad3))
print("----------")
for s in grades.get_students_above(85):
    print(s)
print("----------")
for s in grades.get_students_above(60):
    print(s)
print("----------")
for s in grades.get_students_above(40):
    print(s)
