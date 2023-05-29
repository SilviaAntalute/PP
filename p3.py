from functools import reduce

numbers = [1, 21, 75, 39, 7, 2, 35, 3, 31, 7, 8]

filtered_numbers = list(filter(lambda x: x >= 5, numbers))

paired_numbers = list(zip(filtered_numbers[::2], filtered_numbers[1::2]))

multiplied_numbers = list(map(lambda x: x[0] * x[1], paired_numbers))

result = reduce(lambda x, y: x + y, multiplied_numbers)

print(filtered_numbers)
print(paired_numbers)
print(multiplied_numbers)
print(result)
