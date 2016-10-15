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
from board import ORDER, display_3d_board, display_board, is_board_invalid
import os



def get_rows_trial(check_len, test_slice):
    """Return the trial rows, which are all the ones with # trues <= check_len.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> slice_list = make_lists(board)
    >>> test_slice = slice_list[0][2]
    >>> get_rows_trial(1, test_slice)  # doctest: +NORMALIZE_WHITESPACE
    [[Cell(row: 2, col: 2, box: 3, num: 0, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 1, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 2, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 3, filled: True)]]
    >>> test_slice = slice_list[0][1]
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
    for slice_list in test_slice:
        if slice_list != []:
            if len([i for i in range(ORDER ** 2) if
                    slice_list[i].filled]) <= check_len:
                rows_trial.append(slice_list)
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
    >>> slice_list = make_lists(board)
    >>> test_slice = slice_list[0][2]
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> get_values_block(rows_trial)
    [False, False, False, True]
    >>> test_slice = slice_list[0][1]
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
    >>> slice_list = make_lists(board)
    >>> test_slice = slice_list[0][2]
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> test_combos(1, rows_trial)  # doctest: +NORMALIZE_WHITESPACE
    ([[Cell(row: 2, col: 2, box: 3, num: 0, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 1, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 2, filled: False),
    Cell(row: 2, col: 2, box: 3, num: 3, filled: True)]],
    [False, False, False, True])
    >>> test_slice = slice_list[0][1]
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


def remove_row_val(rows_block, values_block, test_slice_copy, test_slice):
    """Removal:
         rows_block from test_slice copy
         values from all the other rows in test_slice_copy
         values from all the other rows in test_slice
    Modifies everything in-place.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> slice_list = make_lists(board)
    >>> test_slice = slice_list[0][2]
    >>> test_slice_copy = test_slice.copy()
    >>> rows_trial = get_rows_trial(1, test_slice)
    >>> rows_block, values_block = test_combos(1, rows_trial)
    >>> remove_row_val(rows_block, values_block, test_slice_copy, test_slice)
    >>> test_slice_copy  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
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
    >>> test_slice = slice_list[0][1]
    >>> test_slice_copy = test_slice.copy()
    >>> rows_trial = get_rows_trial(2, test_slice)
    >>> rows_block, values_block = test_combos(2, rows_trial)
    >>> remove_row_val(rows_block, values_block, test_slice_copy, test_slice)
    >>> test_slice_copy  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [[Cell(row: 1, col: 2, box: 1, num: 0, filled: True),
    Cell(row: 1, col: 2, box: 1, num: 1, filled: False),
    Cell(row: 1, col: 2, box: 1, num: 2, filled: False),
    Cell(row: 1, col: 2, box: 1, num: 3, filled: True)],
    [Cell(row: 1, col: 3, box: 1, num: 0, filled: True),
    Cell(row: 1, col: 3, box: 1, num: 1, filled: False),
    Cell(row: 1, col: 3, box: 1, num: 2, filled: False),
    Cell(row: 1, col: 3, box: 1, num: 3, filled: True)]]
    """
    loc_list = []
    for row_block in rows_block:
        test_slice_copy.remove(row_block)
        loc_list.append(test_slice.index(row_block))
    for i, value in enumerate(values_block):
        if value:
            for row in test_slice_copy:
                row[i].filled = False
            for j, row in enumerate(test_slice):
                if j not in loc_list:
                    row[i].filled = False


def show_status(board):
    """Showing status function."""
    print('\033[0;0H')  # Move cursor to top of screen
    print('\033[?25l')    # Remove the cursor
    display_board(board)
    count_filled = count_filled_cells(board)
    choices_left = count_choices_left(board)
    print('{} cells unfilled, {} extra choices left\033[K'
          .format(ORDER ** 4 - count_filled, choices_left - ORDER ** 4))


def process_slice(board, tslice, tslice_copy, check_len):
    """Process a single tslice in the test_slices, for a given # of choices.

    Returns the new check length.
    """
    rows_trial = get_rows_trial(check_len, tslice_copy)
    if len(rows_trial) < check_len:
        check_len += 1
    else:
        rows_block, values_block = test_combos(check_len, rows_trial)
        if len(values_block) > 0:
            remove_row_val(rows_block, values_block, tslice_copy, tslice)
        else:
            check_len += 1
    if is_board_invalid(board):
        raise ValueError('Board just went invalid!')
    return check_len


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
    slice_list = make_lists(board)
    add_filled_cells_from_file(slice_list[0])
    count = ORDER ** 6  # total choices for a 'blank' board
    post_iter_count = count_choices_left(board)
    print('\033[2J')  # Clear the screen
    show_status(board)
    pass_num = 0
    done = False
    while post_iter_count < count and not done:
        for itl, test_list in enumerate(slice_list):  # slice_list len = 8
            for its, tslice in enumerate(test_list):
                tslice_copy = tslice.copy()
                check_len = 1
                while (check_len <= len(tslice_copy) and
                       check_len <= 2 and not done):
                    check_len = process_slice(board, tslice,
                                              tslice_copy, check_len)
                    done = count_choices_left(board) == ORDER ** 4
                    pass_num += 1
                    show_status(board)
                    print('pass #: {}, test_list: {}, '
                          'test_slice: {}, check_len: {}\033[K'.
                          format(pass_num, itl, its, check_len))
            if done:
                break
        if done:
            break
        count = post_iter_count
        post_iter_count = count_choices_left(board)
    print('Total passes: {}'.format(pass_num))
    print('\033[?25h')    # Return the cursor



def main():
    pass


if __name__ == '__main__':
    main_test_loop()
