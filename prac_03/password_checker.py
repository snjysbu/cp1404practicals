# Constants
MIN_PASSWORD_LENGTH = 5
MAX_PASSWORD_LENGTH = 15
REQUIRE_SPECIAL_CHAR = True

def is_valid_password(password):
    # Check the length of the password
    if not MIN_PASSWORD_LENGTH <= len(password) <= MAX_PASSWORD_LENGTH:
        return False

    # Initialize flags for character types
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False

    # Check each character in the password
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif REQUIRE_SPECIAL_CHAR and not char.isalnum():
            has_special = True

    # Check if all required character types are present
    if has_digit and has_lower and has_upper and (not REQUIRE_SPECIAL_CHAR or has_special):
        return True
    else:
        return False

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH} characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more numbers")

    if REQUIRE_SPECIAL_CHAR:
        print("    and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\\")

    while True:
        user_password = input("> ")

        if is_valid_password(user_password):
            print(f"Your {len(user_password)} character password is valid: {user_password}")
            break
        else:
            print("Invalid password!")

if __name__ == "__main__":
    main()
