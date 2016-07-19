"""Case conversion between various cases

Handles snake_case, CONSTANT_CASE, kebob-case, CamelCase
Automatically detects case, assuming perfectly-typed

Inputs:  word
Output:  word converted to snake, camel, kebob and constant cases

"""

CASES = ['snake', 'camel', 'kebob', 'constant']


def get_input_word():
    """Get user word, requested to be changed."""
    return input('What is your word? ')


def detect_input_case(word):
    """Detect input case based on word; trow and exception if not detectable.

    >>> detect_input_case('snake_case')
    'snake'
    >>> detect_input_case('CamelCase')
    'camel'
    >>> detect_input_case('kebob-case')
    'kebob'
    >>> detect_input_case('CONSTANT_CASE')
    'constant'
    """
    if '-' in word and word == word.lower():
        print(word, 'kebob')
        return 'kebob'
    elif '_' in word and word == word.upper():
        print(word, 'constant')
        return 'constant'
    elif '_' in word and word == word.lower():
        print(word, 'snake')
        return 'snake'
    elif word[0] == word[0].upper() and word != word.upper() and word.isalpha():
        print(word, 'camel')
        return 'camel'
    else:
        raise ValueError(word)


def convert_camel_to_snake(word):
    """Convert word from camel case to snake case."

    >>> convert_camel_to_snake('CamelCase')
    'camel_case'
    """
    word = word[0].lower() + word[1:]
    word = ''.join([d.replace(d, '_' + d.lower()) if d.isupper() else d
                    for d in word])
    return word


def convert_kebob_to_snake(word):
    """Convert word from kebob case to snake case.

    >>> convert_kebob_to_snake('kebob-case')
    'kebob_case'
    """
    return word.replace('-', '_')


def convert_constant_to_snake(word):
    """Convert word from constant case to snake case.

    >>> convert_constant_to_snake('CONSTANT_CASE')
    'constant_case'
    """
    return word.lower()


def convert_to_snake(word, in_case):
    """Convert word to snake case from input case.

    >>> convert_to_snake('snake_case', 'snake')
    'snake_case'
    >>> convert_to_snake('CamelCase', 'camel')
    'camel_case'
    >>> convert_to_snake('kebob-case', 'kebob')
    'kebob_case'
    >>> convert_to_snake('CONSTANT_CASE', 'constant')
    'constant_case'
    """
    out_word = word
    if in_case == 'camel':
        return convert_camel_to_snake(out_word)
    elif in_case == 'kebob':
        return convert_kebob_to_snake(out_word)
    elif in_case == 'constant':
        return convert_constant_to_snake(out_word)
    else:
        return out_word


def convert_snake_to_camel(word):
    """Convert word from snake case to camel case.

    >>> convert_snake_to_camel('snake_case')
    'SnakeCase'
    """
    return ''.join([w.capitalize() for w in word.split('_')])


def convert_snake_to_kebob(word):
    """Convert word from snake case to kebob case.

    >>> convert_snake_to_kebob('snake_case')
    'snake-case'
    """
    return word.replace('_', '-')


def convert_snake_to_constant(word):
    """Convert word from snake case to constant case.

    >>> convert_snake_to_constant('snake_case')
    'SNAKE_CASE'
    """
    return word.upper()


def convert_from_snake(word, out_case):
    """Convert word to desired case, from snake case

    >>> convert_from_snake('snake_case', 'camel')
    'SnakeCase'
    >>> convert_from_snake('snake_case', 'snake')
    'snake_case'
    >>> convert_from_snake('snake_case', 'kebob')
    'snake-case'
    >>> convert_from_snake('snake_case', 'constant')
    'SNAKE_CASE'
    """
    out_word = word
    if out_case == 'camel':
        return convert_snake_to_camel(out_word)
    elif out_case == 'kebob':
        return convert_snake_to_kebob(out_word)
    elif out_case == 'constant':
        return convert_snake_to_constant(out_word)
    else:
        return out_word


def show_conversions(input_word, snake_word):
    """Display word converted into all CASES

    >>> show_conversions('snake_case', 'snake_case')
    snake_case in snake is snake_case
    snake_case in camel is SnakeCase
    snake_case in kebob is snake-case
    snake_case in constant is SNAKE_CASE
    """
    for output_case in CASES:
        converted_word = convert_from_snake(snake_word, output_case)
        print('{} in {} is {}'.format(input_word, output_case, converted_word))


def main():
    input_word = get_input_word()
    input_case = detect_input_case(input_word)
    snake_word = convert_to_snake(input_word, input_case)
    show_conversions(input_word, snake_word)


if __name__ == '__main__':
    main()
