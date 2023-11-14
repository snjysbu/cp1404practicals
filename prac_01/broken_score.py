def main():
    try:
        score = float(input("Enter your score: "))

        if 0 <= score <= 100:
            score_categories = {
                (90, 100): "Excellent",
                (50, 89): "Passable",
                (0, 49): "Bad"
            }

            for score_range, category in score_categories.items():
                if score >= score_range[0] and score <= score_range[1]:
                    print(category)
                    break
        else:
            print("Invalid score. Please enter a score between 0 and 100.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric score.")


if __name__ == "__main__":
    main()
