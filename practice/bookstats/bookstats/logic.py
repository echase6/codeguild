"""bookstats Logic."""

from . import models


def get_word_count(search: str):
    """  """
    word = models.filter_word(search)
    if word in models.word_counts.keys():
        return models.word_counts[word]
    else:
        return 0


def get_word_frequency(search: str):
    """  """
    word = models.filter_word(search)
    if word in models.word_counts.keys():
        return models.word_counts[word] / models.total_words
    else:
        return 0
