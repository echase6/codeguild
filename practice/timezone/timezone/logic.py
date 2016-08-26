"""timezone Logic."""

from tzwhere import tzwhere
import arrow


def get_time_at_tz(tz_string):
    """Return the current time (as a string) at a given timezone."""
    utc = arrow.utcnow()
    time = utc.to(tz_string)
    time_string = time.format()
    return time_string


def get_tz(input_string):
    r"""Return the time zone given lat, long.

    >>> get_tz('45,45')
    'Europe/Moscow'
    """
    lon_lat_list = input_string.split(',')
    if len(lon_lat_list) != 2:
        raise KeyError('not enough arguments for lat,lng')
    tz = tzwhere.tzwhere(shapely=True)
    tz_sring = tz.tzNameAt(float(lon_lat_list[0]), float(lon_lat_list[1]))
    return tz_sring


def get_time_at_latlng(input_string):
    """Return the time at a given lat, long."""
    tz_string = get_tz(input_string)
    return get_time_at_tz(tz_string)


def get_requested_time(time_string, time_zone):
    """Return an arrow object with a given time and time zone."""
    # if !('/\d{4}-\d{2}-\d{2} \d{2}:\d{2}/'.match(input_string)):
    if False:
        raise KeyError('Time not in YYYY-MM-DD HH:mm format')
    return arrow.get(time_string).replace(tzinfo=time_zone)


def get_formatted_conv_time(arrow_time, time_zone):
    r"""Converts between timezones and strips off only the Y/M/D/H/m

    >>> get_formatted_conv_time(arrow.get('2016-08-23 14:00'), 'America/Boise')
    '2016-08-23 08:00'
    """
    return arrow_time.to(time_zone).format('YYYY-MM-DD HH:mm')
