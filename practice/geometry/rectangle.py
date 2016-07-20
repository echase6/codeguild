""" """


class Rectangle:
    """"""
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        """Return repr()

        >>> repr(Rectangle(3.0, 4.0, 2.1, 8.9))
        'Rectangle(3.0, 4.0, 2.1, 8.9)'
        """
        return 'Rectangle({}, {}, {}, {})'.format(
            self.x,
            self.y,
            self.w,
            self.h
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Rectangle(3.0, 4.0, 2.1, 8.9) == Rectangle(3.00, 4.00, 2.1, 8.9)
        True
        >>> Rectangle(3.0, 4.0, 2.1, 8.9) == Rectangle(4.2, 3.0, 2.3, 7)
        False
        """
        return (
            self.x == other.x and
            self.y == other.y and
            self.w == other.w and
            self.h == other.h
        )
