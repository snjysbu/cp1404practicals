def extract_name(email):
    # Split the email address at the '@' symbol and take the first part
    name = email.split('@')[0]
    # Split the name at '.' and capitalize each part, then join them with a space
    name = ' '.join(part.capitalize() for part in name.split('.'))
    return name

user_data = {}  # Dictionary to store email and name pairs

while True:
    email = input("Email: ")
    if email == "":
        break  # Exit the loop if the user enters a blank email

    name = extract_name(email)
    is_name_correct = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if is_name_correct in ("", "y"):
        user_data[email] = name
    else:
        name = input("Name: ")
        user_data[email] = name

print("\nUser Data:")
for email, name in user_data.items():
    print(f"{name} ({email})")
