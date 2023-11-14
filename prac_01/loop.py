# Display all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print n stars based on user input
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

# Print n lines of increasing stars
n = int(input("Number of lines: "))
for i in range(1, n + 1):
    print('*' * i)
print()

# Print a pattern of numbers
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Print a pattern of letters
import string
letters = string.ascii_uppercase
for i in range(26):
    print(letters[i], end=' ')
    if (i + 1) % 10 == 0:
        print()
