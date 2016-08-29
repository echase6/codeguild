"""jokes Views."""

from . import models
from . import logic
from django.shortcuts import render
from django.http import HttpResponse


def render_submission(request):
    """Render the joke submission page."""
    return render(request, 'jokes/enter_joke.html')


def render_list(request):
    """Show the jokes list."""
    jokes = models.get_all_jokes()
    jokes_list = [
        [joke.setup, joke.punchline]
        for joke in jokes
    ]
    template_data = {
        'jokes': jokes_list
    }
    return render(request, 'jokes/show_jokes.html', template_data)


def render_ack(request):
    """Show the acknowledgment page."""
    try:
        joke_text = request.POST['joke_text']
        joke_punch = request.POST['joke_punchline']
    except KeyError:
        return HttpResponse('missing text', status=400)
    try:
        models.add_joke(joke_text, joke_punch)
    except ValueError:
        return render(request, 'jokes/ack_fail.html')
    return render(request, 'jokes/ack.html')

def render_ack_fail(request):
    """Show the failed-acknowledgement page."""
    return render(request, 'jokes/ack_fail.html')
