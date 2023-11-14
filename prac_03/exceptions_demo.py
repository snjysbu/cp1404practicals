try:
    # Input from the user
    number = int(input("Enter a number: "))

    # Check for division by zero
    if number == 0:
        raise ValueError("Division by zero is not allowed.")

    # Perform the division
    result = 10 / number

    # Attempting to convert a non-integer to an integer
    int("abc")

except ValueError as ve:
    print(f"A ValueError occurred: {ve}")

except ZeroDivisionError:
    print("A ZeroDivisionError occurred when attempting to divide by zero.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print(f"The result is: {result}")

finally:
    print("Execution finished.")
