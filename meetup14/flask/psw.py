# import libraries
import random
import string

# create data for psw generator
lettersL = string.ascii_lowercase
lettersU = string.ascii_uppercase
num = string.digits
special = string.punctuation


def generate_password():
    data = lettersL + lettersU + num + special

    #length = int(input('How long the pasword should be? '))
    #)
    #if length < 8:
    #    print("The psw shoud be at least 8 lenght")   

    psw = random.sample(data, k=10)

    s = ''.join(psw)

    return s