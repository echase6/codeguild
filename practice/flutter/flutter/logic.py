"""flutter Logic."""

from . import models


def get_flutts():
    """Return 10 Flutts for display.

    >>> create_save_new_flutt('Wo', '2016-09-05T11:00')
    Flutt(text:'Wo', date:'2016-09-05T11:00')
    >>> get_flutts()  # doctest: +NORMALIZE_WHITESPACE
    [Flutt(text:'Wo', date:datetime.datetime(2016, 9, 5, 18, 0, tzinfo=<UTC>)),
    Flutt(text:'He', date:datetime.datetime(2016, 9, 5, 17, 0, tzinfo=<UTC>))]
    """
    flutt_list = models.Flutt.objects.all().order_by('-timestamp')
    last_item = min(len(flutt_list), 10)
    return flutt_list[:last_item]


def get_queried_flutts(string):
    """Return 10 Flutts filtered flutts for display.

    >>> get_queried_flutts('o')
    [Flutt(text:'Wo', date:datetime.datetime(2016, 9, 5, 18, 0, tzinfo=<UTC>))]
    """
    flutt_list = models.Flutt.objects.all().order_by('-timestamp')
    filtered_flutts = flutt_list.filter(text__contains=string)
    if len(filtered_flutts) == 0:
        return None
    last_item = min(len(filtered_flutts), 10)
    return filtered_flutts[:last_item]


def create_save_new_flutt(text, timestamp):
    r"""Create a new Flutt, and save to the database.

    >>> create_save_new_flutt('He', '2016-09-05T10:00')
    Flutt(text:'He', date:'2016-09-05T10:00')
    """
    new_flutt = models.Flutt(text=text, timestamp=timestamp)
    new_flutt.save()
    return new_flutt
