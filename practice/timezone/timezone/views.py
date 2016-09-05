"""timezone Views."""
from . import logic
import arrow

from django.http import HttpResponse


def get_qualified_tz(latlng_string):
    """Check the requested lat, lng for validity."""
    lat_lng_list = latlng_string.split(',')
    if len(lat_lng_list) != 2:
        raise KeyError()
    tz_at_latlng = logic.get_tz(lat_lng_list)
    if tz_at_latlng is None:
        raise IOError()
    return tz_at_latlng


def return_local_time(response):
    local_time_string = logic.get_time_at_tz('US/Pacific')
    return HttpResponse('Local time is: ' + local_time_string)


def return_tz_at_latlng(response, latlng):
    try:
        tz_at_latlng = get_qualified_tz(latlng)
    except KeyError:
        return HttpResponse('Need two values', status=400)
    except IOError:
        return HttpResponse('Time Zone does not exist there.', status=404)
    response_string = 'TimeZone at {} is {}'.format(latlng, tz_at_latlng)
    return HttpResponse(response_string)


def return_time_at_latlng(response, latlng):
    try:
        tz_at_latlng = get_qualified_tz(latlng)
    except KeyError:
        return HttpResponse(error, status=400)
    except IOError:
        return HttpResponse('Time Zone does not exist there.', status=404)
    time_at_latlng = logic.get_time_at_latlng(tz_at_latlng)
    response_string = 'Time at {} is {}'.format(latlng, time_at_latlng)
    return HttpResponse(response_string)


def return_converted_time(response, in_time, out_latlng):
    try:
        tz_at_latlng = get_qualified_tz(out_latlng)
    except KeyError:
        return HttpResponse(error, status=400)
    except IOError:
        return HttpResponse('Time Zone does not exist there.', status=404)
    try:
        requested_time = logic.get_requested_time(in_time)
    except arrow.parser.ParserError:
        return HttpResponse('Time is not as expected', status=400)
    out_time = logic.get_conv_time(requested_time, tz_at_latlng)
    response_string = ('When time is {}, it is {} in {}'
                       .format(in_time, out_time, tz_at_latlng))
    return HttpResponse(response_string)
