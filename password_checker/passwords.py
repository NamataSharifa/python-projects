
# Password Strength Checker
# CSE 111 Project
# Enhancement:
# The program provides feedback to users
# on how to improve their password strength.

# Character constants
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
         "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
           "-", "_", "=", "+", "[", "]", "{", "}", "|", ";",
           ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\",
           "`", "~"]


# 1. Check if a word is in a file
def word_in_file(word, filename, case_sensitive=False):

    with open(filename, "r", encoding="utf-8") as file:

        for line in file:
            file_word = line.strip()

            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True

    return False


# 2. Check if a word contains a character type
def word_has_character(word, character_list):

    for character in word:
        if character in character_list:
            return True

    return False


# 3. Calculate word complexity
def word_complexity(word):

    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


# 4. Calculate password strength
def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)

    strength = 1 + complexity

    return strength


# 5. Main function

    
def main():

    password = input("Enter a password to test (q to quit): ")

    while password != "q" and password != "Q":

        strength = password_strength(password)

        print(f"Password strength: {strength}/5")

        # Give suggestions to improve password strength
        if strength == 0:
            print("Suggestion: Choose a password that is not a dictionary word or commonly used password.")

        elif strength == 1:
            print("Suggestion: Make your password at least 10 characters long.")

        elif strength == 2:
            print("Suggestion: Add uppercase letters, numbers, or special symbols.")

        elif strength == 3:
            print("Suggestion: Try adding another type of character.")

        elif strength == 4:
            print("Suggestion: Add another character type to make your password stronger.")

        elif strength == 5:
            print("Excellent! You have a strong password.")

        print()

        password = input("Enter another password to test (q to quit): ")

    print("Goodbye!")



# Start the program
if __name__ == "__main__":
    main()
