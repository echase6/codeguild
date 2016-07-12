"""
Program to translate a single word into Pig Latin, correctly handling
   punctuation and capitalization and handling multiple consonants.
   (Super Advanced Assignment)
This is an individual project by Eric Chase, 7/11/16

Input: a single words
Output:  a word converted into Pig Latin
"""

# setup
VOWELS = ['a', 'e', 'i', 'o', 'u']

# Input
english_input = input("What word would you like translated into Pig Latin: ")

# transform

# First, break into three parts: beginning punct., word, and ending punct.

bi = 0                      # bi will be where the beginning punctuation ends
character = english_input[bi]
while not character.isalpha():
    bi += 1
    character = english_input[bi]

ei = len(english_input) - 1  # ei will be where the ending punctuation begins
character = english_input[ei]
while not character.isalpha():
    ei -= 1
    character = english_input[ei]

beginning_punct = english_input[:bi]
ending_punct = english_input[ei + 1:]
english_word = english_input[bi:ei + 1]

# Now, focus on converting the word into Pig Latin

capitalized = english_word[0] == english_word[0].upper()
english = english_word.lower()

i = 0
letter = english[i]
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
print('{} in Pig Latin is {}{}{}'.format(english_input, beginning_punct,
                                         pig_latin, ending_punct))
