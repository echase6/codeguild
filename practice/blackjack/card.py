class Card:
    """Card class."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        """

        >>> Card('A', 'H')
        Card('A', 'H')
        """
        return 'Card({!r}, {!r})'.format(
            self.rank,
            self.suit
        )

    def __eq__(self, other):
        """

        >>> Card('A', 'H') == Card('A', 'H')
        True
        >>> Card('A', 'H') == Card('2', 'H')
        False
        """
        return(
            self.rank == other.rank and
            self.suit == other.suit
        )
