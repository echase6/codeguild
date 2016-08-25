"""timezone Views."""
from . import logic

from django.http import HttpResponse


def return_local_time(response):
    local_time_string = logic.get_time_at_tz('US/Pacific')
    return HttpResponse('Local time is: ' + local_time_string)


def return_tz_at_latlng(response, input_string):
    try:
        tz_at_latlng = logic.get_tz(input_string)
    except KeyError as error:
        return HttpResponse('TimeZone is not as expected', status = 400)
    response_string = 'TimeZone at {} is {}'.format(input_string, tz_at_latlng)
    return HttpResponse(response_string)


def return_time_at_latlng(response, input_string):
    try:
        time_at_latlng = logic.get_time_at_latlng(input_string)
    except KeyError as error:
        return HttpResponse('TimeZone is not as expected', status = 400)
    response_string = 'Time at {} is {}'.format(input_string, time_at_latlng)
    return HttpResponse(response_string)


def return_converted_time(response, in_latlng_str, in_time_str, out_latlng_str):
    try:
        in_tz = logic.get_tz(in_latlng_str)
    except KeyError as error:
        return HttpResponse('In TimeZone is not as expected', status = 400)
    try:
        out_tz = logic.get_tz(out_latlng_str)
    except KeyError as error:
        return HttpResponse('Out TimeZone is not as expected', status = 400)
    try:
        requested_time = logic.get_requested_time(in_time_str, in_tz)
    except KeyError as error:
        return HttpResponse('Time is not as expected', status = 400)
    out_time = logic.get_formatted_conv_time(requested_time, out_tz)
    response_string = 'When time is {} in {}, it is {} in {}'.format(
        in_time_str, in_tz, out_time, out_tz)
    return HttpResponse(response_string)