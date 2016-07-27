from weapon import Weapon


class Creature:
    """Creature class."""

    def __init__(self, location, health, weapons, icon):
        self.location = location
        self.health = health
        self.weapons = weapons
        self.icon = icon

    def __repr__(self):
        """Return repr()

        >>> repr(Creature((1, 2), 10, [Weapon((5, 5), 5)], '-'))
        'Creature((1, 2), 10, [Weapon((5, 5), 5)], '-')'
        """

        return 'Creature({!r}, {!r}, {!r}, {!r})'.format(
            self.location,
            self.health,
            self.weapons,
            self.icon
        )

    def __eq__(self, other):
        """Check for equality.

        >>> Creature((1, 2), 10, [Weapon((5, 5), 5)], '&') ==
        ... Creature((1, 2), 10, [Weapon((5, 5), 5)], '&')
        True
        >>> Creature((1, 3), 10, [Weapon((5, 5), 5)], '&') ==
        ... Creature((1, 2), 10, [Weapon((5, 5), 5)], '&')
        False
        """
        return (
            self.location == other.location and
            self.health == other.health and
            self.weapons == other.weapons and
            self.icon == other.icon
        )


