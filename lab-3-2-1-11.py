﻿word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word=input("Please user, enter a word: ")
user_word=user_word.upper()

for letter in user_word:
    # Complete the body of the loop.
    if (letter=='A' or letter=='E' or letter=='I' or letter=='O' or letter=='U'):
        continue
    else:
        word_without_vowels=word_without_vowels+letter

# Print the word assigned to word_without_vowels.

print(word_without_vowels)
