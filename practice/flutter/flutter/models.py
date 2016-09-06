"""flutter Models."""

from django.db import models


class Flutt(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField()

    #
    # def __init__(self, text, timestamp):
    #     self.text = text
    #     self.timestamp = timestamp

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Flutt(text:{!r}, date: {!r})'.format(self.text, self.timestamp)