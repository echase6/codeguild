"""
This madlib program uses a text string with {word} tags to:
  1. prompt the user to input relevant words
  2. create and display the resultant sentence.

This is an individual project by Eric Chase, 7/9/16

Inputs:  Text string file containing the tags (madlib_pattern.txt)
         User input of the associated words, taken one at a time.
Ouput: Display of the concatinated sentence.
"""
# 1. Setup
import re


def get_descriptors(file):
    """ Retreive descriptors from text file. """
    with open(file) as f:
        string = f.readline()
    descriptors = re.findall(r'{[a-z]*}*', string)
    return string, descriptors


def get_madlib_words(descriptors):
    """ Ask user for words to fit the descriptors. """
    madlib_words = []
    for word in descriptors:
        word_input_str = re.sub(r'\{|\}', '', word)
        new_word = input('Please give me a ' + word_input_str + ': ')
        madlib_words = madlib_words + [new_word]
    return madlib_words


def subst_words(string, words):
    """ Substitute in words into the string, one at a time. """
    out_str = string
    for new_word in words:
        out_str = re.sub(r'{[a-z]*}', new_word, out_str, count=1)
    return out_str


def main():
    madlib_words = []
    madlib_file = "madlib_pattern.txt"
    madlib_string, madlib_descriptors = get_descriptors(madlib_file)
    madlib_words = get_madlib_words(madlib_descriptors)
    out_str = subst_words(madlib_string, madlib_words)
    print(out_str)


main()
