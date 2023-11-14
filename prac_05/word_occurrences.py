def count_word_occurrences(input_text):
    # Split the input text into words and convert them to lowercase
    words = input_text.lower().split()

    # Create a dictionary to store word counts
    word_counts = {}

    for word in words:
        # Remove punctuation (if any)
        word = word.strip(".,!?")

        # Update the word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find the length of the longest word for formatting
    max_word_length = max(len(word) for word in word_counts)

    # Sort the dictionary by word and print the counts with alignment
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")

# Get input from the user
user_input = input("Enter a string: ")
count_word_occurrences(user_input)
