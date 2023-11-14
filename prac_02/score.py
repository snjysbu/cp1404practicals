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

def main():
    user_score = float(input("Enter your score: "))
    result = calculate_grade(user_score)
    print(f"Your result: {result}")

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    random_result = calculate_grade(random_score)
    print(f"Random result: {random_result}")

if __name__ == "__main__":
    main()
