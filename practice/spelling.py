"""
Program to check whether a word follows the 'i before e, except after c' rule.
This is an individual project by Eric Chase, 7/11/16

Input: a single word
Output: the word and whether it follows the rule or not
"""


def get_user_word():
    """ Get word from user. """
    return input('Word? ')


def get_answer(string):
    """ Determine whether word follows the rule and return answer. """
    i = 0
    answer = 'does'
    while i <= len(string) - 2:
        three_letter = string[i:i + 3]
        if three_letter == 'cie':
            answer = 'doesn\'t'
        if three_letter[1:3] == 'ei' and three_letter[0] != 'c':
            answer = 'doesn\'t'
        i += 1
    return answer


def main():
    trial_word = get_user_word()
    answer = get_answer(trial_word)
    print('{} {} follow the rule'.format(trial_word, answer))


main()
