# Define the initial list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Answers to the questions:
# numbers[0] will be 3
# numbers[-1] will be 2
# numbers[3] will be 1
# numbers[:-1] will be [3, 1, 4, 1, 5, 9]
# numbers[3:4] will be [1]
# 5 in numbers will be True
# 7 in numbers will be False
# "3" in numbers will be False
# numbers + [6, 5, 3] will be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
