# Text Analyzer Tool

# Function to count characters
def count_characters(text):
    print("Total characters:", len(text))

# Function to count words
def count_words(text):
    words = text.split()
    print("Total words:", len(words))

# Function to count vowels
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    print("Total vowels:", count)

# Function to convert to uppercase
def to_uppercase(text):
    print("Uppercase:", text.upper())

# Function to convert to lowercase
def to_lowercase(text):
    print("Lowercase:", text.lower())

# Function to find a word
def find_word(text):
    word = input("Enter word to find: ")
    if word in text:
        print("Word found!")
    else:
        print("Word not found!")

# Main Program
text = input("Enter your text: ")

while True:
    print("\n===== TEXT ANALYZER MENU =====")
    print("1. Count Characters")
    print("2. Count Words")
    print("3. Count Vowels")
    print("4. Convert to Uppercase")
    print("5. Convert to Lowercase")
    print("6. Find a Word")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("❌ Enter number only!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            count_characters(text)
        case 2:
            count_words(text)
        case 3:
            count_vowels(text)
        case 4:
            to_uppercase(text)
        case 5:
            to_lowercase(text)
        case 6:
            find_word(text)
        case 7:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice!")