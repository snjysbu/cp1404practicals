def get_password():
    password = input("Enter your password: ")
    return password

def print_password_asterisks(password):
    asterisks = '*' * len(password)
    print(f"Password: {asterisks}")

def main():
    print("Password Checker")
    password = get_password()
    print_password_asterisks(password)

if __name__ == "__main__":
    main()
