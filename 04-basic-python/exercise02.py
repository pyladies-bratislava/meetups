print('Write 3 numbers:')
numbers = [input() for x in range(3)]

sort = (sorted(numbers))
print(','.join(sort))

# Without sort
print('Write 3 numbers:')
numbers = [int(input()) for x in range(3)]

if numbers[0] > numbers[2]:
    numbers[0], numbers[2] = numbers[2], numbers[0]
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]
if numbers[1] > numbers[2]:
    numbers[1], numbers[2] = numbers[2], numbers[1]

print(list(n for n in numbers))
