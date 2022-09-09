data = []


data.append(int(input("Enter whole number: ")))
data.append(int(input("Enter whole number: ")))
data.append(int(input("Enter whole number: ")))
print(data)

if data[0] >= data[1] and data[0] >= data[2]:
  if data[1] >= data[2]:
    print(data[2], data[1], data[0])
  else:
    print(data[2], data[0], data[1])
elif data[1] >= data [0] and data[1] >= data[2]:
  if data[0] >= data[2]:
    print(data[2], data[0], data[1])
  else:
    print(data[0], data[2], data[1])
elif data[2] >= data[0] and data[2] >=data[1]:
  if data[0] >= data[1]:
    print(data[1], data[0], data[2])
  else:
    print(data[0], data[1], data[2])
else:
  print("I don't know :) ")