# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word por favor: ")

for letter in user_word.upper():
    # Complete the body of the for loop.
    if letter in ['A','E','I','O','U']:
        continue
    else:
        print(letter)
    

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word por favor: ")

for letter in user_word.upper():
    # Complete the body of the loop.
    if letter not in ['A', 'E', 'I', 'O', 'U']:
        word_without_vowels += letter
    else:
        continue

# Print the word assigned to word_without_vowels.
print(word_without_vowels)

