"""
Joins words together and uses separators as requested by the user
This is the product of a collaborative effort between:
Richie Lenninger, Jason Lingel, Katie Nichols and Eric Chase, 7/11/16

Input:  a string of words separated by spaces
Output:  a sentence with the words correctly separated by the requested joiners
"""

# setup
#   none needed

# input
input_string = input('Please enter words separated by a space: ')
input_joiner = input('What joiner do you want to use? ')
input_pair_joiner = input('What pair joiner do you want to use? ')
input_last_joiner = input('What last joiner do you want to use? ')

# transform
word_list = input_string.split()
joiner = input_joiner + ' '
pair_joiner = ' ' + input_pair_joiner + ' '
last_joiner = input_last_joiner + ' '

word_count = len(word_list)
if word_count == 1:
    word_string = word_list[0]
elif word_count == 2:
    word_string = pair_joiner.join(word_list)
else:
    word_string = joiner.join(word_list[:-1])
    word_string = word_string + last_joiner + word_list[-1]

# output
print(word_string)
