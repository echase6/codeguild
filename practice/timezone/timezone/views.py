"""timezone Views."""

from . import logic
import arrow

from django.http import HttpResponse


def get_qualified_tz(latlng_string):
    r"""Check the requested lat, lng for validity.

    >>> get_qualified_tz('45,45')
    'Europe/Moscow'
    >>> get_qualified_tz('4545')
    Traceback (most recent call last):
    ...
    KeyError: 'Need two values'
    >>> get_qualified_tz('45,-125')
    Traceback (most recent call last):
    ...
    OSError: Time Zone does not exist there.
    """
    lat_lng_list = latlng_string.split(',')
    if len(lat_lng_list) != 2:
        raise KeyError('Need two values')
    tz_at_latlng = logic.get_tz(lat_lng_list)
    if tz_at_latlng is None:
        raise OSError('Time Zone does not exist there.')
    return tz_at_latlng


def return_local_time(response):
    """Render local time response, which in this case is for US/Pacific."""
    local_time_string = logic.get_time_at_tz('US/Pacific')
    return HttpResponse('Local time is: ' + local_time_string)


def return_tz_at_latlng(response, latlng):
    """Render the timezone response at a given latitude/longitude."""
    try:
        tz_at_latlng = get_qualified_tz(latlng)
    except KeyError as error:
        return HttpResponse(error, status=400)
    except OSError as error:
        return HttpResponse(error, status=400)
    response_string = 'TimeZone at {} is {}'.format(latlng, tz_at_latlng)
    return HttpResponse(response_string)


def return_time_at_latlng(response, latlng):
    """Render the current time response at a given latitude/longitude."""
    try:
        tz_at_latlng = get_qualified_tz(latlng)
    except KeyError as error:
        return HttpResponse(error, status=400)
    except OSError as error:
        return HttpResponse(error, status=400)
    time_at_latlng = logic.get_time_at_latlng(tz_at_latlng)
    response_string = 'Time at {} is {}'.format(latlng, time_at_latlng)
    return HttpResponse(response_string)


def return_converted_time(response, in_time, out_latlng):
    """Render a response of the time at a different lag/lng from a given time.

    The given time incorporates its own timezone.
    """
    try:
        tz_at_latlng = get_qualified_tz(out_latlng)
    except KeyError as error:
        return HttpResponse(error, status=400)
    except OSError as error:
        return HttpResponse(error, status=400)
    try:
        requested_time = logic.get_requested_time(in_time)
    except arrow.parser.ParserError:
        return HttpResponse('Time is not as expected', status=400)
    out_time = logic.get_conv_time(requested_time, tz_at_latlng)
    response_string = ('When time is {}, it is {} in {}'
                       .format(in_time, out_time, tz_at_latlng))
    return HttpResponse(response_string)
