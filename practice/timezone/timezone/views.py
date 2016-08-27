"""timezone Views."""
from . import logic
import arrow

from django.http import HttpResponse


def return_local_time(response):
    local_time_string = logic.get_time_at_tz('US/Pacific')
    return HttpResponse('Local time is: ' + local_time_string)


def return_tz_at_latlng(response, latlng):
    try:
        tz_at_latlng = logic.get_tz(latlng)
    except IOError as error:
        return HttpResponse(error, status=400)
    except KeyError:
        return HttpResponse('Time Zone does not exist there.', status=404)
    response_string = 'TimeZone at {} is {}'.format(latlng, tz_at_latlng)
    return HttpResponse(response_string)


def return_time_at_latlng(response, latlng):
    try:
        time_at_latlng = logic.get_time_at_latlng(latlng)
    except IOError as error:
        return HttpResponse(error, status=400)
    except KeyError:
        return HttpResponse('Time Zone does not exist there.', status=400)
    response_string = 'Time at {} is {}'.format(latlng, time_at_latlng)
    return HttpResponse(response_string)


def return_converted_time(response, in_time, in_latlng, out_latlng):
    try:
        in_tz = logic.get_tz(in_latlng)
    except IOError as error:
        return HttpResponse('In time {}'.format(error), status=400)
    except KeyError:
        return HttpResponse('In Time Zone does not exist at {}'
                            .format(in_latlng), status=400)
    try:
        out_tz = logic.get_tz(out_latlng)
    except IOError as error:
        return HttpResponse('Out time {}'.format(error), status=400)
    except KeyError:
        return HttpResponse('Out Time Zone does not exist at {}'
                            .format(out_latlng), status=400)
    try:
        requested_time = logic.get_requested_time(in_time, in_tz)
    except arrow.parser.ParserError:
        return HttpResponse('Time is not as expected', status=400)
    out_time = logic.get_conv_time(requested_time, out_tz)
    response_string = ('When time is {} in {}, it is {} in {}'
                       .format(in_time, in_tz, out_time, out_tz))
    return HttpResponse(response_string)
