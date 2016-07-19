""" Individual Practice """

def find_sum_pairs(input_list, input_sum):
    """ Search list of integers, looking for pairs which add to sum.

    >>> find_sum_pairs([-1, 0, 1, 2], 3)
    [[1, 2]]
    >>> find_sum_pairs([-1, 0, 1, 2], 1)
    [[-1, 2], [0, 1]]
    >>> find_sum_pairs([2, -1, 2], 1)
    [[2, -1], [-1, 2]]
    >>> find_sum_pairs([-1, 1, 2, 2], 3)
    [[1, 2], [1, 2]]
    """

    output_pairs = []
    for index, first in enumerate(input_list[:-1]):
        output_pairs += [[first, second] for second in input_list[index + 1:] if first + second == input_sum]
    return output_pairs

