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
    # Create Guitar objects
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00)

    # Test get_age() method
    expected_age1 = 100
    actual_age1 = guitar1.get_age(2022)
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {actual_age1}")

    expected_age2 = 9
    actual_age2 = guitar2.get_age(2022)
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {actual_age2}")

    # Test is_vintage() method
    expected_vintage1 = True
    actual_vintage1 = guitar1.is_vintage(2022)
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {actual_vintage1}")

    expected_vintage2 = False
    actual_vintage2 = guitar2.is_vintage(2022)
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {actual_vintage2}")

if __name__ == "__main__":
    main()
