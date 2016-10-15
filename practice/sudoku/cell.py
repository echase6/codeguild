class Cell:
    """Cell class that represents each cell on the board."""
    def __init__(self, row, col, box, num, filled):
        self.row = row
        self.col = col
        self.box = box
        self.num = num
        self.filled = filled

    def __repr__(self):
        """Return repr() of Cell

        >>> repr(Cell(1, 2, 3, 4, True))
        'Cell(row: 1, col: 2, box: 3, num: 4, filled: True)'
        """
        return 'Cell(row: {}, col: {}, box: {}, num: {}, filled: {})'.format(
            self.row,
            self.col,
            self.box,
            self.num,
            self.filled
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Cell(1, 2, 3, 4, True) == Cell(1, 2, 3, 4, True)
        True
        >>> Cell(1, 2, 3, 4, True) == Cell(1, 2, 3, 3, True)
        False
        """
        return (
            self.row == other.row and
            self.col == other.col and
            self.box == other.box and
            self.num == other.num and
            self.filled == other.filled
        )