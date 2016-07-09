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
madlib_words = []
madlib_file = "madlib_pattern.txt"

# Open the file containing the text string and retrieve the tags
with open(madlib_file) as f:
    madlib_string = f.readline()
madlib_descriptors = re.findall(r'{[a-z]*}*', madlib_string)

# 2. Input
for word in madlib_descriptors:
    word_input_str = re.sub(r'\{|\}', '', word)
    new_word = input('Please give me a ' + word_input_str + ': ')
    madlib_words = madlib_words + [new_word]

# 3. Transform
out_str = madlib_string
for new_word in madlib_words:
    out_str = re.sub(r'{[a-z]*}', new_word, out_str, count=1)

# 4. Output
print(out_str)
