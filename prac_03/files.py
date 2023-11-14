
user_name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(user_name)


with open("name.txt", "r") as file:
    stored_name = file.read()
    print(f"Your name is {stored_name}")


with open("numbers.txt", "r") as file:
    lines = file.readlines()
    num1 = int(lines[0])
    num2 = int(lines[1])
    total = num1 + num2
    print(f"The sum of the first two numbers is {total}")


with open("numbers.txt", "r") as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        number = int(line.strip())
        total += number
    print(f"The sum of all numbers is {total}")
