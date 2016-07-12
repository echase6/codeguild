"""
Program to translate a single word into Pig Latin, correctly handling
   punctuation and capitalization and handling multiple consonants.

This is an individual project by Eric Chase, 7/11/16

Input: a single words
Output:  a word converted into Pig Latin
"""

# setup
VOWELS = ['a', 'e', 'i', 'o', 'u']


def get_english_input():
    """ Get the English Input from the user. """
    return input("What word would you like translated into Pig Latin: ")


def get_beginning_punct_index(char_string):
    """ Returns index where beginning punctionation ends. """
    i = 0
    character = char_string[i]
    while not character.isalpha():
        i += 1
        character = char_string[i]
    return i


def get_ending_punct_index(char_string):
    """ Returns index where ending punctionation begins. """
    i = len(char_string) - 1
    character = char_string[i]
    while not character.isalpha():
        i -= 1
        character = char_string[i]
    return i


def get_beginning_punct(char_string, index):
    """ Return the string of punctuation at the beginning. """
    return char_string[:index]


def get_ending_punct(char_string, index):
    """ Return the string of punctuation at the end. """
    return char_string[index + 1:]


def get_english_word(char_string, beginning_index, ending_index):
    """ Return the word between the two indices. """
    return char_string[beginning_index:ending_index + 1]


def convert_english_to_piglatin(english_word):
    """ Returns a Pig Latin word from an English word """
    capitalized = english_word[0].isupper()
    english_word = english_word.lower() # Will capitalize at the end
    i = 0
    letter = english_word[i]
    while letter not in VOWELS:  # Find where the first consonant is
        i += 1
        letter = english_word[i]
    if i == 0:
        piglatin = english_word + 'yay'
    else:
        piglatin = english_word[i:] + english_word[0:i] + 'ay'
    if capitalized:   # Capitalize the output if the input was
        piglatin = piglatin[0].upper() + piglatin[1:]
    return piglatin


def create_piglatin_output(beginning_punct, word, ending_punct):
    """ Concatinate the punctionation at the beginning and end to the word. """
    return beginning_punct + word + ending_punct


def main():
    english_input = get_english_input()
    beg_index = get_beginning_punct_index(english_input)
    end_index = get_ending_punct_index(english_input)
    beg_punct = get_beginning_punct(english_input, beg_index)
    end_punct = get_ending_punct(english_input, end_index)
    english_word = get_english_word(english_input, beg_index, end_index)
    piglatin_word = convert_english_to_piglatin(english_word)
    piglatin_out = create_piglatin_output(beg_punct, piglatin_word, end_punct)
    print('{} in Pig Latin is {}'.format(english_input, piglatin_out))


main()
