"""flutter Views."""

from django.shortcuts import render
from django.http import JsonResponse
from . import logic
from . import models
import datetime
import pytz


def render_index(request):
    """  Render the flutt listing page."""
    flutts = logic.get_flutts()
    template_args = {
        'flutts': flutts
    }
    return render(request, 'flutter/index.html', template_args)


def render_query(request):
    """Render the item add form."""
    query_text = request.GET['query']
    flutts = logic.get_queried_flutts(query_text)
    template_args = {
        'flutts': flutts
    }
    return render(request, 'flutter/query.html', template_args)


def render_submit(request):
    """Render the submit entry page."""
    return render(request, 'flutter/submit.html')


def render_submit_ack(request):
    post_time = datetime.datetime.now(pytz.utc)
    post_text = request.POST['flutter_text']
    new_flutt = models.Flutt(text=post_text, timestamp=post_time)
    new_flutt.save()
    template_args = {
        'flutt': post_text
    }
    return render(request, 'flutter/submit_ack.html', template_args)

