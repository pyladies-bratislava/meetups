# load libraries
import numpy as np
import pandas as pd
import string
import random

# other usefull modul string features:
"""
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'
"""

# generate PSW a given length
letters = list(string.printable[0:93])
psw = "".join(random.sample(letters, k=8))
print(psw)

# generate PWD a given length by user
letters = list(string.printable)
length = int(input("Enter number of character the psw should have: "))
psw = "".join(random.sample(letters, length))
print(len(psw))
print(psw)
print(len(psw))

# generate PWD a given conditions by user
letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

num = int(input("How many numbers the pwd should have? "))
char = int(input("How many letters the pwd should have? "))
spec = int(input("How many letters the pwd should have? "))

length = num + char + spec

pwd = list("".join(random.sample(numbers, num)) + "".join(random.sample(letters, char)) + "".join(random.sample(special, spec)))
random.shuffle(pwd)
pasword = "".join(pwd)

if length <= 7:
    print("The sum of pwd characters must be at least 8!")
else:
    print(pasword)

# Generate secure random numbers for managing secrets
import secrets

def getPass(length):
    return "".join(secrets.choice(string.ascii_letters + string.digits) for x in range(length))

length = int(input("Enter the length of password: "))
password = getPass(length)
print (password)

# output password and copy to clipboard
import pyperclip 

print('Your unique password has been copied to clipboard.')
pyperclip.copy(password)