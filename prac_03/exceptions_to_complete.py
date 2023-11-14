def main():
    valid_input = False

    while not valid_input:
        try:
            user_input = input("Please enter an integer: ")
            number = int(user_input)  # Try to convert the user input to an integer
            valid_input = True  # Mark the input as valid
        except ValueError:
            # Handle the ValueError when a non-integer is entered
            print("Invalid input. Please enter a valid integer.")

    # Now that we have a valid integer, we can proceed
    result = number * 2
    print(f"The result of doubling the number {number} is {result}.")

if __name__ == "__main__":
    main()
