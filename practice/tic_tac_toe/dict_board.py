"""Implements Tic-Tac-Toe board using dictionary.

Methods:
    calc_winner(self) returns the token (as a string) if there is a winner.
      it uses hidden functions _calc_winner_row_col() and _calc_winner_diag()
    str(self) will return a string for pretty-printing the board.
"""

TOKENS = ['X', 'O']


class DictTTTBoard:
    def __init__(self):
        self._dict = {
            (0, 0): ' ', (1, 0): ' ', (2, 0): ' ',
            (0, 1): ' ', (1, 1): ' ', (2, 1): ' ',
            (0, 2): ' ', (1, 2): ' ', (2, 2): ' ',

        }

    def __repr__(self):
        """Implement repr() function.

        >>> sorted(DictTTTBoard()._dict.items())
        [((0, 0), ' '), ((0, 1), ' '), ((0, 2), ' '), ((1, 0), ' '), \
((1, 1), ' '), ((1, 2), ' '), ((2, 0), ' '), ((2, 1), ' '), ((2, 2), ' ')]
        """
        return 'DictTTTBoard {}'.format(self._dict)

    def __eq__(self, other):
        """Implement the equality function.

        >>> DictTTTBoard() == DictTTTBoard()
        True
        >>> a = DictTTTBoard()
        >>> b = DictTTTBoard()
        >>> a._dict[(0, 0)] = 'X'
        >>> a == b
        False
        """
        return self._dict == other._dict

    def place_token(self, x, y, token):
        """Place a token at x, y location (0, 0 is upper left).

        >>> a = DictTTTBoard()
        >>> a.place_token(1, 1, 'X')
        >>> a._dict[(1, 1)]
        'X'
        """
        self._dict[(x, y)] = token

    def calc_winner(self):
        """Return the token string that has a row, column or diagonal."""
        _winner = self._calc_winner_row_col()
        if _winner is not None:
            return _winner
        _winner = self._calc_winner_diag()
        if _winner is not None:
            return _winner

    def _calc_winner_row_col(self):
        """Return the token string if it occurs in an entire row.
        >>> board = DictTTTBoard()
        >>> board._dict.update({(1, 0): 'O', (1, 1): 'O', (1, 2): 'O'})
        >>> board._calc_winner_row_col()
        'O'
        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 2): 'X', (1, 2): 'X', (2, 2): 'X'})
        >>> board._calc_winner_row_col()
        'X'
        >>> board = DictTTTBoard()
        >>> board._calc_winner_row_col()
        """
        for token in TOKENS:
            for i in range(3):
                if (all([self._dict[(i, j)] == token for j in range(3)]) or
                   all([self._dict[(j, i)] == token for j in range(3)])):
                    return token

    def _calc_winner_diag(self):
        """Return the token string if it occurs in a positive diagonal.
        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 0): 'X', (1, 1): 'X', (2, 2): 'X'})
        >>> board._calc_winner_diag()
        'X'
        >>> board = DictTTTBoard()
        >>> board._calc_winner_diag()
        """
        for token in TOKENS:
            if (all([self._dict[(i, i)] == token for i in range(3)]) or
                    all([self._dict[(2 - i, i)] == token for i in range(3)])):
                return token

    def __str__(self):
        r"""Return a pretty-printed picture of the board.

        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 0): 'X', (1, 0): 'X', (2, 0): 'X',
        ...                     (0, 2): 'O', (2, 1): 'O'})
        >>> board.__str__()  # doctest: +NORMALIZE_WHITESPACE
        'X|X|X\n | |O\nO| | \n'
        """
        out_string = ('\n'.join(
                     ['|'.join(
                         [self._dict[(x, y)]
                          for x in range(3)])
                      for y in range(3)]
                               ) + '\n')
        return out_string
