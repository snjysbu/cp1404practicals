import random

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    return '*' * int(score)

def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Score Program!")

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Select an option: ").strip().lower()

        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            if 'score' not in locals():
                print("Please get a valid score first.")
            else:
                result = calculate_grade(score)
                print(f"Result: {result}")
        elif choice == 's':
            if 'score' not in locals():
                print("Please get a valid score first.")
            else:
                stars = print_stars(score)
                print(f"Stars: {stars}")
        elif choice == 'q':
            print("Thank you for using the Score Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
