

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")  # Creating a named car
    my_car.drive(30)
    print(my_car)

    limo = Car(100, "Limo")  # Creating a named car
    limo.add_fuel(20)
    print(f"{limo.name} has {limo.fuel} units of fuel.")
    limo.drive(115)
    print(f"Attempted to drive {limo.name} 115 km, actual distance driven: {limo.drive(115)} km")
    print(limo)

if __name__ == "__main__":
    main()

