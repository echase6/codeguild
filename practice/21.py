"""
Program to give adivse to someone playing 21 (the card game.)
This is the product of an individual effort by Eric Chase, 7/9/16

Inputs:  Two cards
         (without error checking for valid input)
Output:  The point total amount
         Advise on whether to Hit or Stay, or call out Blackjack!
Note:  Instructions tell to assume Aces are worth 1 point unless it puts the
total over 21.  These are 'soft rules'.
"""
# Set up
point_total = 0
card = ['','']

# Gather inputs
# Could not figure out how to keep inputs on same line as in the example
print('I will give you advise on what to do after your first two cards.')
print('Valid entries are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')
print('What\'s your first card? ',end = '')
card[0] = input()
print('What\'s your second card? ',end = '')
card[1] = input()

# Transform
for i in range(2):
    if card[i] == 'A':
        point_total += 11  # soft dealer rules
    elif card[i] == 'J' or card[i] == 'Q' or card[i] == 'K':
        point_total += 10
    else:
        point_total += int(card[i])
if point_total == 22:  # i.e., two aces, thus one is worth 1 point
        point_total -= 10

if point_total < 17:
    advise_string = 'Hit'
elif point_total < 21:
    advise_string = 'Stay'
else:
    advise_string = 'Blackjack!'

# Output
print(point_total, advise_string)
