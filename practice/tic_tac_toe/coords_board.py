"""Implements Tic-Tac-Toe board using three-element tuples."""

TOKENS = ['X', 'O']


class CoordsTTTBoard:
    def __init__(self):
        self._list = []

    def __repr__(self):
        """Implement repr() function.

        >>> CoordsTTTBoard()
        CoordsTTTBoard []
        """
        return 'CoordsTTTBoard {}'.format(self._list)

    def __eq__(self, other):
        """Implement the equality function.

        >>> CoordsTTTBoard() == CoordsTTTBoard()
        True
        >>> a = CoordsTTTBoard()
        >>> b = CoordsTTTBoard()
        >>> a._list += (0, 0, 'X')
        >>> a == b
        False
        """
        return self._list == other._list

    def place_token(self, x, y, token):
        """Place a token at x, y location (0, 0 is upper left).

        >>> a = CoordsTTTBoard()
        >>> a.place_token(1, 1, 'X')
        >>> a._list
        [(1, 1, 'X')]
        """
        self._list += [(x, y, token)]

    def calc_winner(self):
        """Return the token string that has a row, column or diagonal."""
        _winner = self._calc_winner_row_col()
        _winner += self._calc_winner_diag()
        return _winner

    def _calc_winner_row_col(self):
        """Return the token string if it occurs in an entire row.
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (1, 0, 'X'), (2, 0, 'X')]
        >>> board._calc_winner_row_col()
        'X'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'O'), (0, 1, 'O'), (0, 2, 'O')]
        >>> board._calc_winner_row_col()
        'O'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'O'), (1, 0, 'X'), (2, 0, 'X')]
        >>> board._calc_winner_row_col()
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (2, 0, 'X')]
        >>> board._calc_winner_row_col()
        """
        for token in TOKENS:
            for i in range(3):
                if (all([(j, i, token) in self._list for j in range(3)]) or
                   all([(i, j, token) in self._list for j in range(3)])):
                    return token

    def _calc_winner_diag(self):
        """Return the token string if it occurs in the positive diagonal.
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (1, 1, 'X'), (2, 2, 'X')]
        >>> board._calc_winner_diag()
        'X'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(2, 0, 'O'), (1, 1, 'O'), (0, 2, 'O')]
        >>> board._calc_winner_diag()
        'O'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'O'), (1, 1, 'X'), (2, 2, 'X')]
        >>> board._calc_winner_diag()
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_diag()
        """
        for token in TOKENS:
            if (all([(i, i, token) in self._list for i in range(3)]) or
               all([(2 - i, i, token) in self._list for i in range(3)])):
                return token

    def __str__(self):
        """Return a pretty-printed picture of the board.

        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (1, 0, 'X'), (2, 0, 'X'),
        ...                     (0, 2, 'O'), (2, 1, 'O')]
        >>> board.__str__()  # doctest: +NORMALIZE_WHITESPACE
        X| |O
        X| |
        X|O|
        """
        for i in range(3):
            cell_list = []
            for j in range(3):
                if (i, j, 'X') in self._list:
                    cell_list += ['X']
                elif (i, j, 'O') in self._list:
                    cell_list += ['O']
                else:
                    cell_list += [' ']
            print('|'.join(cell_list))
