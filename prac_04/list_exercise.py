# Function to get user input and calculate statistics
def get_numbers_and_calculate_statistics():
    numbers = []  # Initialize an empty list to store numbers
    for i in range(5):
        number = float(input("Number: "))  # Prompt the user for a number
        numbers.append(number)  # Add the number to the list

    # Output information about the numbers
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

# List of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Function to check if the username is authorized
def check_username_authorization(username):
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    get_numbers_and_calculate_statistics()  # Get numbers and calculate statistics
    username = input("Enter your username: ")  # Prompt the user for a username
    check_username_authorization(username)  # Check username authorization
