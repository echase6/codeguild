"""jokes Models."""


class Joke:
    """Value type that holds a joke's setup and punchline.

    Both setup and punchline are text.
    """

    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __eq__(self, other):
        return self.setup == other.setup and self.punchline == other.punchline

    def __repr__(self):
        return 'Joke: {} {}'.format(self.setup, self.punchline)


_JOKES = []


def get_all_jokes():
    """Return all of the jokes."""
    return _JOKES


def add_joke(setup, punchline):
    """Add the entered joke to the list."""

    if are_both_parts_entered(setup, punchline):
        new_joke = Joke(setup, punchline)
        _JOKES.append(new_joke)
        return new_joke
    else:
        raise ValueError('joke or punchline is invalid')


def are_both_parts_entered(setup, punchline):
    """Check to ensure there is both a setup and punchline."""
    return len(setup) != 0 and len(punchline) != 0
