from random import shuffle
from card import Card


class Deck:
    """Deck class, holds a list of Cards."""

    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """

        >>> Deck([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])
        Deck([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])
        """
        return 'Deck({!r})'.format(
            self.card_list
        )

    def __eq__(self, other):
        """

        >>> (Deck([Card('A', 'H'), Card('A', 'H')]) ==
        ...  Deck([Card('A', 'H'), Card('A', 'H')]))
        True
        >>> (Deck([Card('A', 'H'), Card('A', 'H')]) ==
        ...  Deck([Card('2', 'H'), Card('A', 'H')]))
        False
        """
        return self.card_list == other.card_list

SUITS = ['S', 'D', 'C', 'H']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def initialize_deck():
    """Loads and returns deck with cards in order. """
    deck = Deck([])
    for suit in SUITS:
        for rank in RANKS:
            deck.card_list += [Card(rank, suit)]
    return deck


def shuffle_deck(deck):
    """Shuffles deck.   """
    shuffle(deck.card_list)


def test_is_deck_empty(deck):
    """Tests whether deck is empty and returns True if empty.

    >>> test_is_deck_empty(Deck([Card('2', 'C'), Card('3', 'D')]))
    False
    >>> test_is_deck_empty(Deck([]))
    True
    """
    return len(deck.card_list) == 0
