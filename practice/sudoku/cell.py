class Cell:
    """Cell class that represents each cell on the board."""
    def __init__(self, location, values):
        self.location = location
        self.values = values

    def __repr__(self):
        """Return repr() of Cell

        >>> repr(Cell((1, 2), {1, 2}))
        'Cell((1, 2), {1, 2})'
        """
        return 'Cell({}, {})'.format(
            self.location,
            self.values
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Cell((1, 2), {1, 2}) == Cell((1, 2), {1, 2})
        True
        >>> Cell((1, 2), {1, 2}) == Cell((1, 2), {1, 4})
        False
        """
        return (
            self.location == other.location and
            self.values == other.values
        )