data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200
to_delete = []

#   my rudimentary way of deleting elements from a list
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        to_delete.append(value)
result = [element for element in data if element not in to_delete]

print(result)

