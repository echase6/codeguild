"""flutter Models."""

from django.db import models


class Flutt(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        """String Function.

        >>> str(Flutt(text='Hello', timestamp='2016-09-05T11:00'))
        'Hello'
        """
        return self.text

    def __repr__(self):
        """Magic repr Function.

        >>> repr(Flutt(text='Hello', timestamp='2016-09-05T11:00'))
        "Flutt(text:'Hello', date:'2016-09-05T11:00')"
        """
        return 'Flutt(text:{!r}, date:{!r})'.format(self.text, self.timestamp)
