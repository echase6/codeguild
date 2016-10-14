"""Sudoku solving program.

Will handle 4x4, 9x9 and 16x16 puzzles.
Puzzle comes from the file referenced in board.py (sudoku_.txt)

Algorithm comes from considering the board in a 3-D space, with the 3rd
  dimension being cell contents.  In this manner, the puzzle is solved
  when only one cell-cube is filled when looking at the puzzle-cube from
  each of the 3 sides.

In this manner, each pass though the solving algorithm takes slices of
  the puzzle cube in rows, columns, boxes, and numbers and uses the same
  solver for each slice:
  -- if there are n-slivers holding n unique values, those values can be
     eliminated from all the other slivers in the slice.

Passes are continued until no progress is made on eliminating choices.
"""

from itertools import combinations
from board import make_blank_board, add_filled_cells_from_file
from board import count_choices_left, count_filled_cells, make_lists
from board import ORDER, display_board


def get_rows_trial(check_len, test_slice):
    """Return the trial rows, which are all the ones with # trues <= check_len.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> test_slice = row_list[2]
    >>> get_rows_trial(1, test_slice)  # doctest: +NORMALIZE_WHITESPACE
    [[Cell(row: 2, col: 2, box: 3, num: 0, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 1, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 2, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 3, filled: True)]]
    >>> test_slice = row_list[1]
    >>> get_rows_trial(2, test_slice)  # doctest: +NORMALIZE_WHITESPACE
    [[Cell(row: 1, col: 0, box: 0, num: 0, filled: False),
    Cell(row: 1, col: 0, box: 0, num: 1, filled: True),
    Cell(row: 1, col: 0, box: 0, num: 2, filled: True),
    Cell(row: 1, col: 0, box: 0, num: 3, filled: False)],
    [Cell(row: 1, col: 1, box: 0, num: 0, filled: False),
    Cell(row: 1, col: 1, box: 0, num: 1, filled: True),
    Cell(row: 1, col: 1, box: 0, num: 2, filled: True),
    Cell(row: 1, col: 1, box: 0, num: 3, filled: False)]]
    >>> get_rows_trial(1, test_slice)
    []
    """
    rows_trial = []
    for list in test_slice:
        if list != []:
            if len([i for i in range(ORDER ** 2) if
                    list[i].filled]) <= check_len:
                rows_trial.append(list)
    return rows_trial


def test_for_qty(check_len, values_block):
    """Check for quantity of determined cells in rows_block.
    Returns true if the quantity exists.

    >>> test_for_qty(2, [False, False, False, True])
    True
    >>> test_for_qty(1, [False, True, False, True])
    False

    """
    return sum([1 for value in values_block if value]) <= check_len


def get_values_block(combo):
    """Get a list representing the the values to remove.

    Return empty list if there are too many values
    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> test_slice = row_list[2]
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> get_values_block(rows_trial)
    [False, False, False, True]
    >>> test_slice = row_list[1]
    >>> rows_trial = get_rows_trial(2, test_slice)
    >>> get_values_block(rows_trial)
    [False, True, True, False]
    """
    filled_positions = []
    for i in range(len(combo[0])):
        filled_positions.append(any(
            [row[i].filled for row in combo]))
    return filled_positions


def test_combos(check_len, rows_trial):
    """Test the trial rows.
    Return block of rows if check_len combos exist, empty list otherwise.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> test_slice = row_list[2]
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> test_combos(1, rows_trial)  # doctest: +NORMALIZE_WHITESPACE
    ([[Cell(row: 2, col: 2, box: 3, num: 0, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 1, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 2, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 3, filled: True)]],
    [False, False, False, True])
    >>> test_slice = row_list[1]
    >>> rows_trial = get_rows_trial(2, test_slice)
    >>> test_combos(2, rows_trial)  # doctest: +NORMALIZE_WHITESPACE
    ([[Cell(row: 1, col: 0, box: 0, num: 0, filled: False),
    Cell(row: 1, col: 0, box: 0, num: 1, filled: True),
    Cell(row: 1, col: 0, box: 0, num: 2, filled: True),
    Cell(row: 1, col: 0, box: 0, num: 3, filled: False)],
    [Cell(row: 1, col: 1, box: 0, num: 0, filled: False),
    Cell(row: 1, col: 1, box: 0, num: 1, filled: True),
    Cell(row: 1, col: 1, box: 0, num: 2, filled: True),
    Cell(row: 1, col: 1, box: 0, num: 3, filled: False)]],
    [False, True, True, False])
    """
    combos = combinations(rows_trial, check_len)
    for combo in combos:
        values = get_values_block(combo)
        if test_for_qty(check_len, values):
            return list(combo), values
    return [[]], []


def remove_values(values_block, test_list):
    """Remove the values in values_block from the test_list
    The successful rows should have already been removed from the test_list
    Edits test_list in-place

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> test_slice = row_list[2]
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> rows_block, values_block = test_combos(1, rows_trial)
    >>> remove_rows(rows_block, test_slice)
    >>> remove_values(values_block, test_slice)
    >>> test_slice  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [[Cell(row: 2, col: 0, box: 2, num: 0, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 1, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 2, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 3, filled: False)],
    [Cell(row: 2, col: 1, box: 2, num: 0, filled: True),
    Cell(row: 2, col: 1, box: 2, num: 1, filled: True),
    Cell(row: 2, col: 1, box: 2, num: 2, filled: True),
    Cell(row: 2, col: 1, box: 2, num: 3, filled: False)],
    [Cell(row: 2, col: 3, box: 3, num: 0, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 1, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 2, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 3, filled: False)]]
    """
    for i, value in enumerate(values_block):
        if value:
            for row in test_list:
                row[i].filled = False


def remove_rows(rows_block, test_slice):
    """Remove the rows in rows_block from rows_trial
    Edits rows_trial in-place.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> test_slice = row_list[2]
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> rows_block, foo = test_combos(1, rows_trial)
    >>> remove_rows([], test_slice)
    >>> test_slice  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [[Cell(row: 2, col: 0, box: 2, num: 0, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 1, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 2, filled: True),
    ...
    Cell(row: 2, col: 3, box: 3, num: 2, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 3, filled: True)]]
    >>> remove_rows(rows_block, test_slice)
    >>> test_slice  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [[Cell(row: 2, col: 0, box: 2, num: 0, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 1, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 2, filled: True),
    Cell(row: 2, col: 0, box: 2, num: 3, filled: True)],
    [Cell(row: 2, col: 1, box: 2, num: 0, filled: True),
    Cell(row: 2, col: 1, box: 2, num: 1, filled: True),
    Cell(row: 2, col: 1, box: 2, num: 2, filled: True),
    Cell(row: 2, col: 1, box: 2, num: 3, filled: True)],
    [Cell(row: 2, col: 3, box: 3, num: 0, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 1, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 2, filled: True),
    Cell(row: 2, col: 3, box: 3, num: 3, filled: True)]]
    """
    for row_block in rows_block:
        try:
            test_slice.remove(row_block)
        except ValueError:
            pass


def show_status(board, row_list, post_iter_count):
    """Showing status function."""
    display_board(board)
    count_filled = count_filled_cells(row_list)
    print('{} cells filled, {} choices left.'
          .format(count_filled, post_iter_count))


def main_test_loop():
    """This is where the work is taking place.

    The algorithm is:
    -- For each row/col/box/num list:
        -- Set check_len = 1
        -- Make a copy of the list, since parts will be removed
        -- Loop until check_len > # rows left (or some arbitrary ending value)
            -- Set rows_trial equal to the rows with filled_count <= check_len
            -- If # rows_trial < check_len, skip to next check_len
            -- Test all combinations of rows_trial for #values <= check_len
            -- True:
                -- remove successful values from the other rows in master
                -- remove successful values from the other rows in the copy
                -- remove successful combinations from the copy
            -- False:
                -- increment check_len
            -- go back to beginning of loop
    -- Check for progress in filling cells; if any was made, start over.
    """
    board = make_blank_board()
    row_list, col_list, box_list, num_list = make_lists(board)
    add_filled_cells_from_file(row_list)
    count = ORDER ** 6  # total choices for a 'blank' board
    post_iter_count = count_choices_left(board)
    show_status(board, row_list, post_iter_count)
    while post_iter_count < count:
        print('top while loop')
        for test_list in [row_list, col_list, box_list, num_list]:
            print(
                'lens, row: {}, col: {}, box: {}, num: {}'.format(len(row_list),
                                                                  len(col_list),
                                                                  len(box_list),
                                                                  len(
                                                                      num_list)))
            print('second for loop')
            for test_slice in test_list:
                test_slice_copy = test_slice.copy()
                print('third for loop, len test_slice: {}'.format(
                    test_slice_copy))
                check_len = 1
                while check_len <= len(test_slice_copy) and check_len < 4:
                    print('fourth while loop')
                    rows_trial = get_rows_trial(check_len, test_slice_copy)
                    print('len rows_trial: {}'.format(len(rows_trial)))
                    if len(rows_trial) < check_len:
                        check_len += 1
                    else:
                        rows_block, values_block = test_combos(check_len,
                                                               rows_trial)
                        if len(rows_block) > 0:
                            remove_rows(rows_block, test_slice_copy)
                            remove_values(values_block, test_slice_copy)
                            remove_values(values_block, test_slice)
                        else:
                            check_len += 1
        count = post_iter_count
        post_iter_count = count_choices_left(board)
        show_status(board, row_list, post_iter_count)


def main():
    pass


if __name__ == '__main__':
    main_test_loop()
