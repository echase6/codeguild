"""timezone Views."""

from . import logic
import arrow

from django.http import HttpResponse


def get_qualified_lat_lng(latlng_string):
    r"""Get the requested lat, lng, checking for validity.

    >>> get_qualified_lat_lng('45,45')
    45, 45
    >>> get_qualified_lat_lng('4545')
    Traceback (most recent call last):
    ...
    ValueError: 'Need two values'
    """
    lat_lng_list = [float(num) for num in latlng_string.split(',')]
    if len(lat_lng_list) != 2:
        raise ValueError('Need two values')
    if (-90 < lat_lng_list[0] < 83) and (-180 < lat_lng_list[1] < 179):
        return lat_lng_list[0], lat_lng_list[1]
    else:
        raise ValueError('lat or lng are out of bounds')


def return_local_time(response):
    """Render local time response, which in this case is for US/Pacific."""
    local_time_string = logic.get_time_at_tz('US/Pacific')
    return HttpResponse('Local time is: ' + local_time_string)


def return_tz_at_latlng(response, latlng):
    """Render the timezone response at a given latitude/longitude."""
    try:
        lat, lng = get_qualified_lat_lng(latlng)
    except ValueError as error:
        return HttpResponse(error, status=400)
    try:
        tz_at_latlng = logic.get_tz(lat, lng)
    except ValueError as error:
        return HttpResponse(error, status=400)
    response_string = 'TimeZone at {} is {}'.format(latlng, tz_at_latlng)
    return HttpResponse(response_string)


def return_time_at_latlng(response, latlng):
    """Render the current time response at a given latitude/longitude."""
    try:
        lat, lng = get_qualified_lat_lng(latlng)
    except ValueError as error:
        return HttpResponse(error, status=400)
    try:
        tz_at_latlng = logic.get_tz(lat, lng)
    except ValueError as error:
        return HttpResponse(error, status=400)
    time_at_latlng = logic.get_time_at_tz(tz_at_latlng)
    response_string = 'Time at {} is {}'.format(latlng, time_at_latlng)
    return HttpResponse(response_string)


def get_requested_time(time_string):
    """Return an arrow object with a given time and time zone."""
    return arrow.get(time_string)


def return_converted_time(response, in_time, latlng):
    """Render a response of the time at a different lag/lng from a given time.

    The given time incorporates its own timezone.
    """
    try:
        lat, lng = get_qualified_lat_lng(latlng)
    except ValueError as error:
        return HttpResponse(error, status=400)
    try:
        tz_at_latlng = logic.get_tz(lat, lng)
    except ValueError as error:
        return HttpResponse(error, status=400)
    try:
        requested_time = get_requested_time(in_time)
    except arrow.parser.ParserError:
        return HttpResponse('Time is not as expected', status=400)
    out_time = logic.get_conv_time(requested_time, tz_at_latlng)
    response_string = ('When time is {}, it is {} in {}'
                       .format(in_time, out_time, tz_at_latlng))
    return HttpResponse(response_string)
