"""
Joins words together and uses separators
This is the product of a collaborative effort between:
Richie Lenninger, Jason Lingel, Katie Nichols and Eric Chase, 7/11/16

Input:  a string of words separated by spaces
Output:  a sentence with the words correctly separeated by commas, 'and'
"""

# setup
#   none needed

# input
input_string = input('Please enter words separated by a space: ')

# transform
word_list = input_string.split()

word_count = len(word_list)
if word_count == 1:
    word_string = word_list[0]
elif word_count == 2:
    word_string = ' and '.join(word_list)
else:
    word_string = ', '.join(word_list[:-1])
    word_string = word_string + ', and ' + word_list[-1]

# output
print(word_string)
