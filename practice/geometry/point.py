""" """


class Point:
    """Point class holds x and y coordinates of a point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return repr()

        >>> repr(Point(3.0, 4.0))
        'Point(3.0, 4.0)'
        """
        return 'Point({}, {})'.format(
            self.x,
            self.y
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Point(3.0, 4.0) == Point(3.00, 4.00)
        True
        >>> Point(3.0, 4.0) == Point(4.0, 3.0)
        False
        """
        return (
            self.x == other.x and
            self.y == other.y
        )
