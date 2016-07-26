from card import Card


class Hand:
    """Hand class, holds a list of Cards."""

    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """

        >>> Hand([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])
        Hand([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])
        """
        return 'Hand({!r})'.format(
            self.card_list
        )

    def __eq__(self, other):
        """

        >>> (Hand([Card('A', 'H'), Card('A', 'H')]) ==
        ...  Hand([Card('A', 'H'), Card('A', 'H')]))
        True
        >>> (Hand([Card('A', 'H'), Card('A', 'H')]) ==
        ...  Hand([Card('2', 'H'), Card('A', 'H')]))
        False
        """
        return self.card_list == other.card_list


def add_card_to_hand(card, hand):
    """Adds a card to the hand, modifying it in-place.

    >>> hand = Hand([Card('2', 'C'), Card('3', 'D')])
    >>> add_card_to_hand(Card('A', 'H'), hand)
    >>> hand
    Hand([Card('2', 'C'), Card('3', 'D'), Card('A', 'H')])
    """
    hand.card_list += [card]

def return_score_of_hand(hand):
    """Calculates and returns the score of a hand.

    >>> return_score_of_hand(Hand([Card('2', 'C'), Card('3', 'D')]))
    5
    >>> return_score_of_hand(Hand([Card('A', 'C'), Card('A', 'D')]))
    12
    >>> return_score_of_hand(Hand([Card('K', 'C'), Card('A', 'D')]))
    21
    >>> return_score_of_hand(Hand([Card('K', 'C'), Card('10', 'D'),
    ...                            Card('A', 'D'), Card('A', 'D')]))
    22
    """
    point_total = 0
    num_aces_11 = 0
    for card in hand.card_list:
        if card.rank == 'A':
            point_total += 11
            num_aces_11 += 1
        elif card.rank == 'J' or card.rank == 'Q' or card.rank == 'K':
            point_total += 10
        else:
            point_total += int(card.rank)
    while num_aces_11 > 0 and point_total > 21:
        point_total -= 10
        num_aces_11 -= 1
    return point_total
