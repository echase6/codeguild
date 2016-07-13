""" Credit Card validator """

def get_card_num():
    """ Get card number from user. """
    valid_input = input('What is your credit card number? ')
    if valid_input == '':
        valid_input = '4556737586899855'
    return valid_input


def get_check_digit(input_string):
    """ Return the check digit.

    >>> get_check_digit("456789")
    9
    """
    check_digit = input_string[-1]
    return int(check_digit)

def make_digit_list(input_string):
    """ Return list of digits with the last digit removed.

    >>> make_digit_list("12345")
    [1, 2, 3, 4]

    """

    new_string = input_string[:-1]
    return list(map(int, new_string))


def reverse_digits(digit_list):
    """ Reverse the digits in a list

    >>> reverse_digits([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return list(reversed(digit_list))

def double_odd_digits(digit_list):
    """ Double the digits in the odd indices

    >>> double_odd_digits([1, 2, 3, 4])
    [2, 2, 6, 4]
    """
    for index, digit in enumerate(digit_list):
        if index % 2 == 0:
            digit_list[index] *= 2
    return digit_list


def subtract_nine(digit_list):
    """ Subtract 9 from all digits greater than 9.

    >>> subtract_nine([18, 2, 10, 0])
    [9, 2, 1, 0]
    """
    for index, digit in enumerate(digit_list):
        if digit > 9:
            digit_list[index] -= 9
    return digit_list


def calc_check_sum(digit_list):
    """ Calculate the 1's digit of the check sum.

    >>> calc_check_sum([9, 2, 1, 0])
    2

    """
    sum_digits = sum(digit_list)
    return sum_digits % 10

def notify_user(check_digit, check_sum):
    """ Test value and print whether it matches. """


    if check_digit == check_sum:
        print('Valid!')
    else:
        print('Invalid!')


def main():
    credit_card_num = get_card_num()
    check_digit = get_check_digit(credit_card_num)
    test_digit_list = make_digit_list(credit_card_num)
    reversed_digits = reverse_digits(test_digit_list)
    doubled_odd_digits = double_odd_digits(reversed_digits)
    subtracted_nine_digits = subtract_nine(doubled_odd_digits)
    check_sum = calc_check_sum(subtracted_nine_digits)
    notify_user(check_digit, check_sum)

main()
