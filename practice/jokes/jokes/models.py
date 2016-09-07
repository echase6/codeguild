"""jokes Models."""


class Joke:
    """Value type that holds a joke's setup and punchline.

    Both setup and punchline are text.
    """
    def __init__(self, setup, punchline):
        r""" Initialize new Joke.

        >>> a = Joke('knock-knock', 'who 1 dat?')
        >>> a.setup
        'knock-knock'
        >>> a.punchline
        'who 1 dat?'
        """
        self.setup = setup
        self.punchline = punchline

    def __eq__(self, other):
        r""" Test for equality.

        >>> a = Joke('knock-knock', 'who dat?')
        >>> b = Joke('blah blah blah', 'blah!')
        >>> a == a
        True
        >>> a == b
        False
        """
        return self.setup == other.setup and self.punchline == other.punchline

    def __repr__(self):
        r""" Magic repr function.

        >>> Joke('knock-knock', 'who dat?')
        Joke('knock-knock', 'who dat?')
        """
        return 'Joke({!r}, {!r})'.format(self.setup, self.punchline)


_JOKES = []


def get_all_jokes():
    r"""Return all of the jokes.

    >>> get_all_jokes()
    [Joke('knock-knock', 'who 2 dat?'), Joke('bahbah', 'blacksheep')]
    """
    return _JOKES


def add_joke(setup, punchline):
    r"""Add the entered joke to the list.

    >>> add_joke('knock-knock', 'who 2 dat?')
    Joke('knock-knock', 'who 2 dat?')
    >>> add_joke('bahbah', 'blacksheep')
    Joke('bahbah', 'blacksheep')
    >>> _JOKES
    [Joke('knock-knock', 'who 2 dat?'), Joke('bahbah', 'blacksheep')]
    >>> add_joke('', '')
    Traceback (most recent call last):
    ...
    ValueError: joke or punchline is invalid
    """
    if _are_both_parts_entered(setup, punchline):
        new_joke = Joke(setup, punchline)
        _JOKES.append(new_joke)
        return new_joke
    else:
        raise ValueError('joke or punchline is invalid')


def _are_both_parts_entered(setup, punchline):
    r"""Check to ensure there is both a setup and punchline.

    >>> _are_both_parts_entered('','')
    False
    >>> _are_both_parts_entered('knock-knock', 'who dat?')
    True
    """
    return len(setup) != 0 and len(punchline) != 0
