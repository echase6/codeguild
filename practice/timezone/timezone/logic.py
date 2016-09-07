"""timezone Logic."""

from tzwhere import tzwhere
import arrow

tz = tzwhere.tzwhere()

def get_time_at_tz(tz_string):
    """Return the current time (as a string) at a given timezone."""
    utc = arrow.utcnow()
    time_string = str(utc.to(tz_string))
    return time_string


def get_tz(lat, lng):
    r"""Return the time zone given lat, long.

    >>> get_tz(45,45)
    'Europe/Moscow'
    >>> get_tz(45,-125)
    Traceback (most recent call last):
    ...
    KeyError: Time Zone does not exist there.
    """
    # tz = tzwhere.tzwhere()
    tz_string = tz.tzNameAt(lat, lng)
    if tz_string is None:
        raise ValueError('Time Zone does not exist there.')
    return tz_string


def get_conv_time(arrow_time, time_zone):
    r"""Converts between timezones

    >>> str(get_conv_time(arrow.get('2016-08-23 14:00'), 'America/Boise'))
    '2016-08-23T08:00:00-06:00'
    """
    return arrow_time.to(time_zone)
