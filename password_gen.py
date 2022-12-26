"""Built in modules"""
from string import (ascii_lowercase,ascii_uppercase,digits,punctuation)
from random import choices

def password_generator():
    """This function generates automatic password for users"""

    lower_case = ascii_lowercase
    upper_case = ascii_uppercase
    numbers = digits
    symbols = punctuation

    temp_password = ''

    print('''Welcome to Edu8Africa Password Generator Application''')

    while True:
        try:
            length = int(input("Enter Password Length: "))
            if length >= 12:
                password = temp_password.join(choices(
                    upper_case+lower_case+numbers+symbols, k=length))
                print(f'Your unique password is: {password}')
                print(len(password))
            else:
                print("Password length Should be at least 12 Characters long ")

            break
        except ValueError:
            print('Please Enter a whole number')
    print('''Thank you for using this Application\n
    ********** Developed by Andrews Asamoah **********''')


password_generator()
