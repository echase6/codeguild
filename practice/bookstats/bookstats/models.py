"""bookstats Models."""
import re

FILENAME = 'bookstats/book.txt'

def filter_word(word):
    filter = re.sub(r'\W+$', '', word)
    filter = re.sub(r'^\W+', '', filter)
    return filter.lower()


def load_book():
    """  """
    with open(FILENAME) as book_file:
        book_text = book_file.read()

    word_list = book_text.split()
    word_count = {}
    total_words = 0

    for raw_word in word_list:
        word = filter_word(raw_word)
        if word != '':
            total_words += 1
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count, total_words


word_counts, total_words = load_book()