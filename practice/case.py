""" Case conversion between various cases
This is an individual project by Eric Chase, 7/13/16

Inputs:  word and desired output Case
Output:  word converted to snake, camel, kebob and constant cases

"""

def get_input_word():
    """ Get user word, requested to be changed. """
    return input('What is your word? ')


def detect_input_case(word):
    """ Detect input case based on word

    >>> detect_input_case('snake_case')
    'snake'
    >>> detect_input_case('CamelCase')
    'camel'
    >>> detect_input_case('kebob-case')
    'kebob'
    >>> detect_input_case('CONSTANT_CASE')
    'constant'
    """
    if '-' in word:
        return 'kebob'
    elif '_' in word:
        if word[0].isupper():
            return 'constant'
        else:
            return 'snake'
    else:
        return 'camel'


def convert_to_snake(word, in_case):
    """ Convert word to snake case from input case.

    >>> convert_to_snake('snake_case', 'snake')
    'snake_case'
    >>> convert_to_snake('CamelCase', 'camel')
    'camel_case'
    >>> convert_to_snake('kebob-case', 'kebob')
    'kebob_case'
    >>> convert_to_snake('CONSTANT_CASE', 'constant')
    'constant_case'
    """
    out_word = []
    if in_case == 'snake':
        out_word = word
    elif in_case == 'camel':
        out_word = word[0].lower()
        out_word += ''.join([d.replace(d, '_' + d.lower())
                             if d.isupper() else d for d in word[1:]])
    elif in_case == 'kebob':
        out_word = word.replace('-', '_')
    else:  # i.e., 'constant'
        out_word = word.lower()
    return out_word


def convert_from_snake(word, out_case):
    """ Convert word to desired case, from snake case

    >>> convert_from_snake('snake_case', 'camel')
    'SnakeCase'
    >>> convert_from_snake('snake_case', 'snake')
    'snake_case'
    >>> convert_from_snake('snake_case', 'kebob')
    'snake-case'
    >>> convert_from_snake('snake_case', 'constant')
    'SNAKE_CASE'
    """
    if out_case == 'snake':
        out_word = word
    elif out_case == 'camel':
        out_word = ''.join([w.capitalize() for w in word.split('_')])
    elif out_case == 'kebob':
        out_word = word.replace('_', '-')
    else:  # i.e., 'constant'
        out_word = word.upper()
    return out_word


def main():
    input_word = get_input_word()
    input_case = detect_input_case(input_word)
    snake_word = convert_to_snake(input_word, input_case)
    for output_case in ['snake', 'camel', 'kebob', 'constant']:
        converted_word = convert_from_snake(snake_word, output_case)
        print('{} in {} is {}'.format(input_word, output_case, converted_word))


if __name__ == '__main__':
    main()
