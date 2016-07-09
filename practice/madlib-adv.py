"""
This program creates and displays a sentence based on a user's
input of a noun, an adverb, an adjectivee and an exclamation.
The template comes from Stern and Price's original Mad Libs book.

This is an individual project by Eric Chase, 7/9/16

Inputs:  Four strings
Ouput: Display of the concatinated sentence.
"""
# 1. Setup

# 2. Input
print('Please provide... ')
noun_str = input('a noun: ')
adverb_str = input('an adverb: ')
adjective_str = input('an adjective: ')
exclamation_str = input('an exclamation: ')
exclamation_str = exclamation_str.upper()

# 3. Transform
out_str = (exclamation_str + '! he said ' + adverb_str +
           ' as he jumped into his convertible ' + noun_str +
           ' and drove off with his ' + adjective_str + ' wife.')

# 4. Output
print(out_str)
