"""import string and random built in modules"""
from string import (ascii_lowercase, ascii_uppercase, digits, punctuation)
from random import choices

def password_generator():
    """This function generates automatic password for users"""

    print('Welcome to Edu8Africa Password Generator Application\n')

    while True:
        try:
            # typecasting the string input to integer
            length = int(input("Enter Password Length: "))
            if length >= 12:
                # initialized an empty string and added random values
                # from the string module based on the user input
                password = ''.join(choices(ascii_uppercase+ascii_lowercase+digits+punctuation, k=length))
                print(f'Your unique password is: {password}')
            else:
                print("Password length Should be at least 12 Characters long ")

            break
        except ValueError:
            print('Please Enter a whole number')
    print('''Thank you for using this Application\n
    ********** Developed by Andrews Asamoah **********''')


password_generator()
