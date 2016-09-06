"""bookstats Views."""

from django.shortcuts import render
from django.http import JsonResponse
from . import logic



def render_html(request):
    """ """
    return render(request, 'bookstats/index.html')


def return_json(request):
    """  """
    query_word = request.GET.get('word')
    json_data = {
        'word': query_word,
        'word_count': logic.get_word_count(query_word),
        'word_freq': logic.get_word_frequency(query_word)
    }
    return JsonResponse(json_data)
