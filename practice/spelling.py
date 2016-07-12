"""
Program to check whether a word follows the 'i before e, except after c' rule.
This is an individual project by Eric Chase, 7/11/16

Input: a single word
Output: the word and whether it follows the rule or not
"""

# setup
#  no setup needed

# input
trial_word = input('Word? ')

# transform
i = 0
answer = 'does'
while i <= len(trial_word) - 2:
    three_letter = trial_word[i:i + 3]
    if three_letter == 'cie':
        answer = 'doesn\'t'
    if three_letter[1:3] == 'ei' and three_letter[0] != 'c':
        answer = 'doesn\'t'
    i += 1

# Output
print('{} {} follow the rule'.format(trial_word, answer))
