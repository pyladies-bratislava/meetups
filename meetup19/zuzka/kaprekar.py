"""The number 6174 is known as Kaprekar's constant, after the mathematician who discovered an associated property, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.

Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.
"""
# Write starting number
num = input("Please enter whole number (at least 4 digits): ")

# check if the number met the reguirements
while len(num) != 4:
    num = input("Please enter 4 digits whole number:")


# smaler number
asc = int("".join(sorted(str(num))))

des = int("".join(sorted(str(num), reverse=True)))

# calculation
x = des - asc

counter = 0

while x != 6174:
    asc = int("".join(sorted(str(x))))
    des = int("".join(sorted(str(x), reverse=True)))
    x = int(des - asc)
    counter = counter + 1

print(counter)
