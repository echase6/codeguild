"""Implements Tic-Tac-Toe board using list of lists."""

TOKENS = ['X', 'O']


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
        self._rows[y][x] = token

    def calc_winner(self):
        """Return the token string that has a row, column or diagonal."""
        _winner = self._calc_winner_row_col()
        if _winner is not None:
            return _winner
        _winner = self._calc_winner_diag()
        if _winner is not None:
            return _winner

    def _calc_winner_row_col(self):
        """Return the token string if it occurs in an entire column.
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['X', 'O', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_row_col()
        'X'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', 'O', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_row_col()
        'O'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_row_col()
        """
        for token in TOKENS:
            for i in range(3):
                if (all([self._rows[i][j] == token for j in range(3)]) or
                   all([self._rows[j][i] == token for j in range(3)])):
                    return token

    def _calc_winner_diag(self):
        """Return the token string if it occurs in a positive diagonal.
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        >>> board._calc_winner_diag()
        'X'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', 'O', 'O'], ['O', 'O', 'X']]
        >>> board._calc_winner_diag()
        'O'
        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['O', ' ', 'O'], ['X', 'O', ' ']]
        >>> board._calc_winner_diag()
        """
        for token in TOKENS:
            if (all([self._rows[i][i] == token for i in range(3)]) or
               all([self._rows[2 - i][i] == token for i in range(3)])):
                return token

    def __str__(self):
        """Return a pretty-printed picture of the board.

        >>> board = ListTTTBoard()
        >>> board._rows = [['X', ' ', 'O'], ['X', ' ', ' '], ['X', 'O', ' ']]
        >>> board.__str__()  # doctest: +NORMALIZE_WHITESPACE
        X| |O
        X| |
        X|O|
        """
        out_string = ''
        for row in self._rows:
            out_string += '|'.join(row) + '\n'
        return out_string
