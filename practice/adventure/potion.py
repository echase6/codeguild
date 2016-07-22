class Potion:
    """Potion class."""

    def __init__(self, location, health, icon):
        self.location = location
        self.health = health
        self.icon = icon

    def __repr__(self):
        """Return repr()

        >>> repr(Potion((1, 2), 10, 'g'))
        "Potion((1, 2), 10, 'g')"
        """

        return 'Potion({!r}, {!r}, {!r})'.format(
            self.location,
            self.health,
            self.icon
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Potion((1, 2), 10, 'g') == Potion((1, 2), 10, 'g')
        True
        >>> Potion((1, 3), 10, 'g') == Potion((1, 2), 10, 'g')
        False
        """
        return (
            self.location == other.location and
            self.health == other.health and
            self.icon == other.icon
        )


