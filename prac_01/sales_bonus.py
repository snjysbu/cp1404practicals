def main():
    """
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
    """

    while True:
        sales = float(input("Enter sales: $"))

        if sales < 0:
            break  # Exit the loop if a negative number is entered

        if sales < 1000:
            bonus_percentage = .10
        else:
            bonus_percentage = .15

        bonus = (sales * bonus_percentage) / 100
        print(f"Bonus: ${bonus:.2f}")

if __name__ == "__main__":
    main()
