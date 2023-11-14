def get_incomes(num_months):
    incomes = []
    for month in range(1, num_months + 1):
        try:
            income = float(input(f"Enter income for month {month}: "))
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
            income = 0  # Set a default value for invalid input
        incomes.append(income)
    return incomes
