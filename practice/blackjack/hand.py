class Hand:
    """Hand class, holds a list of Cards."""

    def __init__(self, card_list):
        self.card_list = card_list

    def __repr__(self):
        """

        >>> Hand([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])
        Hand([Card('A', 'H'), Card('A', 'H'), Card('A', 'H')])        """
        return 'Hand({!r})'.format(
            self.card_list
        )

    def __eq__(self, other):
        """

        >>> Hand([Card('A', 'H'), Card('A', 'H')]) == Deck([Card('A', 'H'), Card('A', 'H')])
        True
        >>> Hand([Card('A', 'H'), Card('A', 'H')]) == Deck([Card('2', 'H'), Card('A', 'H')])
        False
        """
        return self.card_list == other.card_list
