class ListTTTBoard:
    def __init__(self):
        self._rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def __repr__(self):
        """Implement repr() function.

        >>> ListTTTBoard()
        ListTTTBoard [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        """
        return 'ListTTTBoard {}'.format(self._rows)

    def __eq__(self, other):
        """Implement the equality function.

        >>> ListTTTBoard() == ListTTTBoard()
        True
        >>> a = ListTTTBoard()
        >>> b = ListTTTBoard()
        >>> a._rows[0][0] = 'X'
        >>> a == b
        False
        """
        return self._rows == other._rows

    def place_token(self, x, y, token):
        """Place a token at x, y location (0, 0 is upper left).

        >>> a = ListTTTBoard()
        >>> a.place_token(1, 1, 'X')
        >>> a._rows
        [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
        """
        self._rows[x][y] = token

    def calc_winner(self):
        """Return the token string that has a row, column or diagonal."""
        _winner = self._calc_winner_row()
        _winner += self._calc_winner_col()
        _winner += self._calc_winner_diag_p()
        _winner += self._calc_winner_diag_n()
        return _winner

    def _calc_winner_row(self):
        """Return the token string if it occurs in an entire row.
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', 'O', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_row()
        'O'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_row()
        """
        winner_token = None
        for row in self._rows:
            token = row[0]
            if (token == row[1] and
               token == row[2] and
               token != ' '):
                winner_token = token
        return winner_token

    def _calc_winner_col(self):
        """Return the token string if it occurs in an entire column.
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['X', 'O', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_col()
        'X'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_col()
        """
        winner_token = None
        for col_index in range(3):
            token = self._rows[0][col_index]
            if (token == self._rows[1][col_index] and
               token == self._rows[2][col_index] and
               token != ' '):
                winner_token = token
        return winner_token

    def _calc_winner_diag_p(self):
        """Return the token string if it occurs in a positive diagonal.
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        >>> board._calc_winner_diag_p()
        'X'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_diag_p()
        """
        token = self._rows[0][0]
        if (token == self._rows[1][1] and
           token == self._rows[2][2] and
           token != ' '):
            return token
        else:
            return

    def _calc_winner_diag_n(self):
        """Return the token string if it occurs in a negative diagonal.
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', 'O', 'O'], ['O', 'O', 'X']]
        >>> board._calc_winner_diag_n()
        'O'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_diag_n()
        """
        token = self._rows[0][2]
        if (token == self._rows[1][1] and
           token == self._rows[2][0] and
           token != ' '):
            return token
        else:
            return

    def __str__(self):
        """Return a pretty-printed picture of the board.

        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['X', ' ', ' '], ['X', 'O', ' ']]
        >>> board.__str__()  # doctest: +NORMALIZE_WHITESPACE
        X| |O
        X| |
        X|O|
        """
        for row in self._rows:
            print('|'.join(row))


