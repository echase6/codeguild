class DictTTTBoard:
    def __init__(self):
        self._dict = {
            (0, 0): ' ', (1, 0): ' ', (2, 0): ' ',
            (0, 1): ' ', (1, 1): ' ', (2, 1): ' ',
            (0, 2): ' ', (1, 2): ' ', (2, 2): ' ',

        }

    def __repr__(self):
        """Implement repr() function.

        >>> DictTTTBoard()
        DictTTTBoard {(0, 0): ' ', (1, 0): ' ', (2, 0): ' ', (0, 1): ' ', \
(1, 1): ' ', (2, 1): ' ', (0, 2): ' ', (1, 2): ' ', (2, 2): ' '}
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
        _winner = self._calc_winner_row()
        _winner += self._calc_winner_col()
        _winner += self._calc_winner_diag_p()
        _winner += self._calc_winner_diag_n()
        return _winner

    def _calc_winner_row(self):
        """Return the token string if it occurs in an entire row.
        >>> board = DictTTTBoard()
        >>> board._dict.update({(1, 0): 'O', (1, 1): 'O', (1, 2): 'O'})
        >>> board._calc_winner_row()
        'O'
        >>> board = DictTTTBoard()
        >>> board._calc_winner_row()
        """
        winner_token = None
        for i in range(3):
            token = self._dict[(i, 0)]
            if (token == self._dict[(i, 1)] and
               token == self._dict[(i, 2)] and
               token != ' '):
                winner_token = token
        return winner_token

    def _calc_winner_col(self):
        """Return the token string if it occurs in an entire column.
        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 2): 'X', (1, 2): 'X', (2, 2): 'X'})
        >>> board._calc_winner_col()
        'X'
        >>> board = DictTTTBoard()
        >>> board._calc_winner_col()
        """
        winner_token = None
        for i in range(3):
            token = self._dict[(0, i)]
            if (token == self._dict[(1, i)] and
               token == self._dict[(2, i)] and
               token != ' '):
                winner_token = token
        return winner_token

    def _calc_winner_diag_p(self):
        """Return the token string if it occurs in a positive diagonal.
        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 0): 'X', (1, 1): 'X', (2, 2): 'X'})
        >>> board._calc_winner_diag_p()
        'X'
        >>> board = DictTTTBoard()
        >>> board._calc_winner_diag_p()
        """
        token = self._dict[(0, 0)]
        if (token == self._dict[(1, 1)] and
           token == self._dict[(2, 2)] and
           token != ' '):
            return token
        else:
            return

    def _calc_winner_diag_n(self):
        """Return the token string if it occurs in a negative diagonal.
        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 2): 'O', (1, 1): 'O', (2, 0): 'O'})
        >>> board._calc_winner_diag_n()
        'O'
        >>> board = DictTTTBoard()
        >>> board._calc_winner_diag_n()
        """
        token = self._dict[(2, 0)]
        if (token == self._dict[(1, 1)] and
           token == self._dict[(0, 2)] and
           token != ' '):
            return token
        else:
            return

    def __str__(self):
        """Return a pretty-printed picture of the board.

        >>> board = DictTTTBoard()
        >>> board._dict.update({(0, 0): 'X', (0, 1): 'X', (0, 2): 'X',
        ...                     (2, 0): 'O', (1, 2): 'O'})
        >>> board.__str__()  # doctest: +NORMALIZE_WHITESPACE
        X| |O
        X| |
        X|O|
        """
        for i in range(3):
            print('|'.join([self._dict[(j, i)] for j in range(3)]))
