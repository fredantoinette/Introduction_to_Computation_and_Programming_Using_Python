"""
Write a function is_in that accepts two strings as arguments and returns True 
if either string occurs anywhere in the other, and False otherwise. Hint: You 
might want to use the built-in str operator in.
"""

def is_in(str1, str2):
    if str1.lower() in str2.lower() or str2.lower() in str1.lower():
        return True
    return False

# test    
print(is_in('test', 'This is a TEST'))
print(is_in('This is a test', 'TEST'))
print(is_in('This is a ...', 'test Python'))
print(is_in('nothing', 'This is a test'))
print(is_in('test code', 'This is a test'))
print(is_in('', 'abc 123'))



"""
Write a function to test is_in.
"""

def test_is_in(str1_inputs, str2_inputs):
    for s1 in str1_inputs:
        for s2 in str2_inputs:
            result = is_in(s1, s2)
            if result == False:
                result_message = 'Either string does not occur anywhere in the other'
            else:
                result_message = 'Okay'
            print(f'string 1: {s1}; string 2: {s2}; result: {result_message}')
            
str1_inputs = ('Python programming', 'Test', 'learning Functions', '')
str2_inputs = ('This is a test', 'I am learning Python', 'This is about functions', '---')
test_is_in(str1_inputs, str2_inputs)
