def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    num_items = get_positive_integer("Number of items: ")

    total_price = 0

    for i in range(num_items):
        price = get_non_negative_float(f"Price of item {i + 1}: $")
        total_price += price

    if total_price > 100:
        total_price *= 0.9  # Apply a 10% discount if the total price is over $100

    formatted_total_price = "${:.2f}".format(total_price)
    print(f"Total price for {num_items} items is {formatted_total_price}")


if __name__ == "__main__":
    main()
