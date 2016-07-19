"""
Program to give adivse to someone playing 21 (the card game.)
This is the product of an individual effort by Eric Chase, 7/9/16
Refactored to use functions 7/12/16

Inputs:  Two cards
         (without error checking for valid input)
Output:  The point total amount
         Advise on whether to Hit or Stay, or call out Blackjack!
Note:  Instructions tell to assume Aces are worth 1 point unless it puts the
total over 21.  These are 'soft rules'.
"""


def display_initial_message():
    """ Tell the user what is happening and which entries are valid. """
    print('I will give you advise on what to do after your first two cards.')
    print('Valid entries are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')
    return


def get_card():
    """ Get the card from the user. """
    return input('What\'s your card? ').upper()


def calc_point_total(cards):
    """ Calculate sum of points, owing to Aces being 1 or 11. """
    point_total = 0
    for i in range(len(cards)):
        if cards[i] == 'A':
            point_total += 11  # soft dealer rules
        elif cards[i] == 'J' or cards[i] == 'Q' or cards[i] == 'K':
            point_total += 10
        else:
            point_total += int(cards[i])
    if point_total == 22:  # i.e., two aces, thus one is worth 1 point
        point_total -= 10
    return point_total


def get_advise(point_total):
    """ Return advise string based on point total. """
    if point_total < 17:
        return 'Hit'
    elif point_total < 21:
        return 'Stay'
    else:
        return 'Blackjack!'


def main():
    card = ['', '']
    display_initial_message()
    card[0] = get_card()
    card[1] = get_card()
    point_total = calc_point_total(card)
    advise = get_advise(point_total)
    print(point_total, advise)

main()
