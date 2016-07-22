from hand import Hand
from card import Card


class Player:
    """Player class."""

    def __init__(self, name, hand, score):
        self.name = name
        self.hand = hand
        self.score = score

    def __repr__(self):
        """

        >>> Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5)
        Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5)
        """
        return 'Player({!r}, {!r}, {!r})'.format(
            self.name,
            self.hand,
            self.score
        )

    def __eq__(self, other):
        """

        >>> (Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5) ==
        ...  Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5))
        True
        >>> (Player('Eric', Hand([Card('2', 'C'), Card('3', 'C')]), 5) ==
        ...  Player('Eric', Hand([Card('2', 'H'), Card('3', 'C')]), 5))
        False
        """
        return(
            self.name == other.name and
            self.hand == other.hand and
            self.score == other.score
        )

PLAYER_NAMES = ['Eric', 'Dealer']


def initialize_players():
    """Set up players and return list of them.

    >>> initialize_players()
    [Player('Eric', Hand([]), 0), Player('Dealer', Hand([]), 0)]
    """
    players = []
    for player_name in PLAYER_NAMES:
        player = Player(player_name, Hand([]), 0)
        players += [player]
    return players
