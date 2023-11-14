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
    print("My guitars!")

    # Create an empty list to store guitars
    guitars = []

    # Sample guitar details
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar} worth ${guitar.cost:.2f}{vintage}")

if __name__ == "__main__":
    main()
