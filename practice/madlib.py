"""
This program creates and displays a sentence based on a user's
input of two nouns and one adjective.
Inputs:  Three strings
Ouput: Display of the concatinated sentence.
"""
#1. Setup

#2. Input
print('Please provide two nouns and an adjective:')
noun_1 = input()
noun_2 = input()
adjective = input()

#3. Transform
out_str = 'The ' + noun_1 + ' jumped over the ' + adjective + ' ' + noun_2 + '.'

#4. Output
print(out_str)
