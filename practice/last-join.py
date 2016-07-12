"""
Joins words together and uses separators as requested by the user
This is the product of a collaborative effort between:
Richie Lenninger, Jason Lingel, Katie Nichols and Eric Chase, 7/11/16
Refactored to use functions 7/12/16

Input:  a string of words separated by spaces
Output:  a sentence with the words correctly separated by the requested joiners
"""


def get_user_input():
    """ Get the user input in the form of a string. """
    return input('Please enter words separated by a space: ')


def get_user_joiner(string):
    """ Get the specific joiner from the the user. """
    print('What {} do you want to use? '.format(string))
    return input()


def create_output(string, joiner, pair_joiner, last_joiner):
    """ Create the output string using the inputs. """
    word_list = string.split()
    word_count = len(word_list)
    if word_count == 1:
        word_string = word_list[0]
    elif word_count == 2:
        word_string = pair_joiner.join(word_list)
    else:
        word_string = joiner.join(word_list[:-1])
        word_string = word_string + last_joiner + word_list[-1]
    return word_string


def main():
    input_string = get_user_input()
    joiner = get_user_joiner('joiner') + ' '
    pair_joiner = ' ' + get_user_joiner('pair joiner') + ' '
    last_joiner = get_user_joiner('last joiner') + ' '
    word_string = create_output(input_string, joiner, pair_joiner, last_joiner)
    print(word_string)


main()
