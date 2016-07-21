class Player:
    """Player class."""

    def __init__(self, name, hand, score, is_staying):
        self.name = name
        self.hand = hand
        self.score = score
        self.is_staying = is_staying

    def __repr__(self):
        """

        >>> Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5, False)
        'Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5, False
        """
        return 'Player({!r}, {!r}, {!r}, {!r})'.format(
            self.name,
            self.hand,
            self.score,
            self.is_staying
        )

    def __eq__(self, other):
        """

        >>> (Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5, False) ==
        ...  Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5, False)
        True
        >>> (Player('Eric', Hand([Card('2', 'C'), Card('3', 'C')]), 5, False) ==
        ...  Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5, False)
        False
        """
        return(
            self.name == other.name and
            self.hand == other.hand and
            self.score == other.score and
            self.is_staying == other.is_staying
        )
