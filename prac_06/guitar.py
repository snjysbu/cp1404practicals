class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50

def main():
    current_year = 2022

    # Create Guitar objects
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Fender Stratocaster", 1954, 2150.80)

    # Print guitar details and check if they are vintage
    print(guitar1)
    print(f"Is guitar1 vintage? {guitar1.is_vintage(current_year)}")
    print()
    print(guitar2)
    print(f"Is guitar2 vintage? {guitar2.is_vintage(current_year)}")

if __name__ == "__main__":
    main()
