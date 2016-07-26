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
        _winner = self._calc_winner_row()
        _winner += self._calc_winner_col()
        _winner += self._calc_winner_diag_p()
        _winner += self._calc_winner_diag_n()
        return _winner

    def _calc_winner_row(self):
        """Return the token string if it occurs in an entire row.
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (1, 0, 'X'), (2, 0, 'X')]
        >>> board._calc_winner_row()
        'X'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'O'), (1, 0, 'X'), (2, 0, 'X')]
        >>> board._calc_winner_row()
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (2, 0, 'X')]
        >>> board._calc_winner_row()
        """
        winner_token = None
        for i in range(3):
            for token in ['X', 'O']:
                if ((0, i, token) in self._list and
                   (1, i, token) in self._list and
                   (2, i, token) in self._list):
                    winner_token = token
        return winner_token

    def _calc_winner_col(self):
        """Return the token string if it occurs in an entire column.
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (0, 1, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_col()
        'X'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'O'), (0, 1, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_col()
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_col()
        """
        winner_token = None
        for i in range(3):
            for token in ['X', 'O']:
                if ((i, 0, token) in self._list and
                   (i, 1, token) in self._list and
                   (i, 2, token) in self._list):
                    winner_token = token
        return winner_token

    def _calc_winner_diag_p(self):
        """Return the token string if it occurs in the positive diagonal.
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (1, 1, 'X'), (2, 2, 'X')]
        >>> board._calc_winner_diag_p()
        'X'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'O'), (1, 1, 'X'), (2, 2, 'X')]
        >>> board._calc_winner_diag_p()
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_diag_p()
        """
        winner_token = None
        for token in ['X', 'O']:
            if ((0, 0, token) in self._list and
               (1, 1, token) in self._list and
               (2, 2, token) in self._list):
                winner_token = token
        return winner_token

    def _calc_winner_diag_n(self):
        """Return the token string if it occurs in the positive diagonal.
        >>> board = CoordsTTTBoard()
        >>> board._list = [(2, 0, 'X'), (1, 1, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_diag_n()
        'X'
        >>> board = CoordsTTTBoard()
        >>> board._list = [(2, 0, 'O'), (0, 1, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_diag_n()
        >>> board = CoordsTTTBoard()
        >>> board._list = [(0, 0, 'X'), (0, 2, 'X')]
        >>> board._calc_winner_diag_n()
        """
        winner_token = None
        for token in ['X', 'O']:
            if ((2, 0, token) in self._list and
               (1, 1, token) in self._list and
               (0, 2, token) in self._list):
                winner_token = token
        return winner_token

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
