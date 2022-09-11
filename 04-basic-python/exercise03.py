"""Write a program that draws a triangle formed of asterisks on the screen. The size is input from the user"""

size = int(input('What is the size of your triangle? '))
for i in range(1, size + 1):
    print('*' * i)

for i in range(size, 1, -1):
    print('*' * i)

for i in range(1, size + 1, 2):
    try:
        spaces = int((5 - i)/2)
    except ZeroDivisionError:
        spaces = 0
    print(' ' * spaces + '*' * i + ' ' * spaces)
