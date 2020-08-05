"""The number 6174 is known as Kaprekar's constant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.

Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.
"""
while True:
    number = input('Enter a 4-digit number with at least 2 distinct digits:')

    try:
        new_int = int(number)
    except ValueError:
        print('incorrect input')
        continue
       
    if len(number) == 4:
        if len(set(number))>=2:
            digit_check = True
            break
        else:
            print('incorrect input')
            continue
    else:
        print('incorrect input')
        continue

N=0

while new_int != 6174:
    number_str = str(new_int)
    if len(number_str)<4:
        missing = 4 - len(number_str)
        for x in range(missing):
            number_str = number_str + '0'

    number_list = list(number_str)
    asc_list = sorted(number_list, reverse=False)
    desc_list = sorted(number_list, reverse=True)

    asc_int = int(''.join(asc_list))
    desc_int = int(''.join(desc_list))

    if desc_int > asc_int:
        asc_int = -asc_int
    else:
        desc_int = -desc_int

    new_int = desc_int + asc_int
    print(desc_int, '+ (', asc_int, ') =', new_int)
    N += 1

print("It took", N, "subtractions to get Kaprekar's constant form the number ", number)
