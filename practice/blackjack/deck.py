class Deck:
    """Deck class, holds a list of Cards."""

    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """

        >>> Deck([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])
        Deck([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])        """
        return 'Deck({!r})'.format(
            self.card_list
        )

    def __eq__(self, other):
        """

        >>> Deck([Card('A', 'H'), Card('A', 'H')]) == Deck([Card('A', 'H'), Card('A', 'H')])
        True
        >>> Deck([Card('A', 'H'), Card('A', 'H')]) == Deck([Card('2', 'H'), Card('A', 'H')])
        False
        """
        return self.card_list == other.card_list
