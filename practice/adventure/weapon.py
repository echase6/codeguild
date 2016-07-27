class Weapon:
    """Weapon class."""

    def __init__(self, location, damage, icon):
        self.location = location
        self.damage = damage
        self.icon = icon

    def __repr__(self):
        """Return repr()

        >>> repr(Weapon((1, 2), 10, '^'))
        "Weapon((1, 2), 10, '^')"
        """

        return 'Weapon({!r}, {!r}, {!r})'.format(
            self.location,
            self.damage,
            self.icon
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Weapon((1, 2), 10, '^') == Weapon((1, 2), 10, '^')
        True
        >>> Weapon((1, 3), 10, '^') == Weapon((1, 2), 10, '^')
        False
        """
        return (
            self.location == other.location and
            self.damage == other.damage and
            self.icon == other.icon
        )


