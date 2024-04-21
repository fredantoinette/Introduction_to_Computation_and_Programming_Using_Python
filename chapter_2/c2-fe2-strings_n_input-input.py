"""
Write code that asks the user to enter their birthday in the form mm/dd/yyyy,
and then prints a string of the form 'You were born in the year yyyy.'
"""

dob = input('Enter your date of birth in the form mm/dd/yyyy: ')
try:
    if 1 <= int(dob[0:2]) <= 12 and 1 <= int(dob[3:5]) <= 31 and int(dob[6:10]) >= 0 \
        and dob[2] == '/' and dob[5] == '/':
            print(f'You were born in the year {dob[-4:]}.')
    else:
        raise Exception("Invalid number input")
except ValueError:
    print("Invalid string input")
    