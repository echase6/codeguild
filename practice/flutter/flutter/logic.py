"""flutter Logic."""

from . import models


def get_flutts():
    """Return 10 Flutts for display.

    >>> create_save_new_flutt('Hello', '2016-09-05')
    >>> get_flutts()
    [Flutt(text: 'Hello', date: '2016-09-05')]
    """
    flutt_list = models.Flutt.objects.all().order_by('-timestamp')
    last_item = min(len(flutt_list), 10)
    return flutt_list[:last_item]


def get_queried_flutts(string):
    """Return 10 Flutts filtered flutts for display.


    """
    flutt_list = models.Flutt.objects.all().order_by('-timestamp')
    filtered_flutts = flutt_list.filter(text__contains=string)
    if len(filtered_flutts) == 0:
        return None
    last_item = min(len(filtered_flutts), 10)
    return filtered_flutts[:last_item]


def create_save_new_flutt(text, timestamp):
    r"""Create a new Flutt, and save to the database.


    """
    new_flutt = models.Flutt(text=text, timestamp=timestamp)
    new_flutt.save()
    return new_flutt