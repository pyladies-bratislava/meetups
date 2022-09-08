import random
import string

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
digits = string.digits
special_char = string.punctuation
chars = upper_letters + lower_letters + digits + special_char

random_range = False

while random_range == False:
    random_range = int(random.choice(digits))
    if random_range < 4:
        random_range = False
        continue
    else:
        break

random_conditions = [random.choice(upper_letters), 
        random.choice(lower_letters), 
        random.choice(digits), 
        random.choice(special_char)]
        
random_no_cond = []

for idx in range(random_range):
    random_no_cond.append(random.choice(chars))

password = random_conditions + random_no_cond
random.shuffle(password)
password = ''.join(password)
print(password)
