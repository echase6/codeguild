"""flutter Views."""

from django.shortcuts import render
from django.utils import timezone
from . import logic


def render_index(request):
    """Render the flutt listing page."""
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
    """Render the submission acknowledgement page.

    This is going to show the Flutter with a time/date stamp.
    """
    post_time = timezone.now()
    post_text = request.POST['flutter_text']
    new_flutt = logic.create_save_new_flutt(post_text, post_time)
    template_args = {
        'flutt': new_flutt
    }
    return render(request, 'flutter/submit_ack.html', template_args)

