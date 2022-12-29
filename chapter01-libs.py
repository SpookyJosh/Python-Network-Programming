from random import randint
from random import choice
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

num_upper = randint(5,10)
print(f"Adding {num_upper} uppercase letters to the password")
num_lower = randint(5,10)
print(f"Adding {num_lower} lowercase letters to the password")
num_digits = randint(5,10)
print(f"Adding {num_digits} digits to the password")

def add_to_password(num_to_include, choices):
    temp = ""
    for i in range(num_to_include):
        temp = temp + str(choice(choices))
    return temp
uppers = add_to_password(num_upper, ascii_uppercase)
lowers = add_to_password(num_lower, ascii_lowercase)
numbers = add_to_password(num_digits, digits)

pwd = uppers+lowers+numbers
print(f"Your password is {pwd}")
