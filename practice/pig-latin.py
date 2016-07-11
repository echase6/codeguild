"""
Program to translate a single word into Pig Latin
This is an individual project by Eric Chase, 7/11/16

Input: a single words
Output:  a word converted into Pig Latin
"""
# setup
VOWELS = ['a', 'e', 'i', 'o', 'u']
# Input
english_word = input("What word would you like translated into Pig Latin: ")

# transform
capitalized = english_word[0] == english_word[0].upper()
english = english_word.lower()

i = 0
letter = english[0]
while letter not in VOWELS:  # Find where the first consonant is
    i += 1
    letter = english[i]
if i == 0:
    pig_latin = english + 'yay'
else:
    pig_latin = english[i:] + english[0:i] + 'ay'
if capitalized:
    pig_latin = pig_latin[0].upper() + pig_latin[1:]

# Output
print('{} in Pig Latin is {}'.format(english_word, pig_latin))
