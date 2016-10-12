class Cell:
    """Cell class that represents each cell on the board."""
    def __init__(self, values, row, col):
        self.values = values
        self.row = row
        self.col = col

    def __repr__(self):
        """Return repr() of Cell

        >>> repr(Cell({1, 2}, 1, 3))
        'Cell(values: {1, 2}, row: 1, col: 3)'
        """
        return 'Cell(values: {}, row: {}, col: {})'.format(
            self.values,
            self.row,
            self.col
        )

    def __eq__(self, other):
        """Check for equality.

        >>> (Cell({1, 2}, 1, 3)) == (Cell({1, 2}, 1, 3))
        True
        >>> (Cell({1, 2}, 1, 3)) == (Cell({1, 2}, 1, 2))
        False
        """
        return (
            self.values == other.values and
            self.row == other.row and
            self.col == other.col
        )