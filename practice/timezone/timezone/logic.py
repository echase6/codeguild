"""timezone Logic."""

from tzwhere import tzwhere
import arrow


def get_time_at_tz(tz_string):
    """Return the current time (as a string) at a given timezone."""
    utc = arrow.utcnow()
    time_string = str(utc.to(tz_string))
    return time_string


def get_tz(lat_lng_list):
    r"""Return the time zone given lat, long.

    >>> get_tz('45,45')
    'Europe/Moscow'
    """
    tz = tzwhere.tzwhere()
    tz_string = tz.tzNameAt(float(lat_lng_list[0]), float(lat_lng_list[1]))
    return tz_string


def get_time_at_latlng(tz_string):
    """Return the time at a given lat, long."""
    return get_time_at_tz(tz_string)


def get_requested_time(time_string):
    """Return an arrow object with a given time and time zone."""
    return arrow.get(time_string)


def get_conv_time(arrow_time, time_zone):
    r"""Converts between timezones

    >>> str(get_conv_time(arrow.get('2016-08-23 14:00'), 'America/Boise'))
    '2016-08-23T08:00:00-06:00'
    """
    return arrow_time.to(time_zone)
