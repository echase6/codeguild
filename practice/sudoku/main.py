"""Sudoku solving program.

Will handle 4x4, 9x9 and 16x16 puzzles.
Puzzle comes from the file referenced in board.py (sudoku_.txt)

Algorithm uses two methods:
-- Exclusionary:  This eliminates choices based on members in the row, col, box.
     This currently takes singles and pairs.
-- Inclusion:  This ascertains what possibilities exist based on missing members
     the other members of the row, col, box
"""


from cell import Cell
from board import make_blank_board, add_filled_cells_from_file
from board import count_choices_left, count_filled_cells, make_lists
from board import ORDER, display_board


def exclude_cell_all(cell, cell_list):
    """Apply exclusionary rule to cell in row, col, box for singles and pairs.

    Exclusion means eliminate choices if a neighbor has that choice as its value
    Also, handle pairs, etc.

    >>> ORDER = 2
    >>> board = (
    ... [[Cell({'1'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})],
    ...  [Cell({'1', '2'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})],
    ...  [Cell({'2'}), Cell({'1', '3'}), Cell({'4'}), Cell({'3', '4'})],
    ...  [Cell({'4'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]])
    >>> exclude_cell_all(0, 0, Cell({'1'}), board)
    >>> board
    [[Cell({'1'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})], \
[Cell({'2'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})], \
[Cell({'2'}), Cell({'1', '3'}), Cell({'4'}), Cell({'3', '4'})], \
[Cell({'4'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]]
    """
    # cell_list = row_col_box_contents(i, j, board)
    if len(cell.values) == 1:
        for sub_cell in cell_list:
            sub_cell.values = sub_cell.values.difference(cell.values)

    elif len(cell.values) == 2:
        for sub_cell in cell_list:
            if sub_cell.values == cell.values:
                for sub2_cell in cell_list:
                    if sub2_cell != sub_cell:
                        sub2_cell.values = sub2_cell.values.difference(
                            cell.values)


def fill_cells_exclude(board):
    """Use exclusionary rule to fill cells."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            cell_list = row_col_box_contents(i, j, board)
            exclude_cell_all(cell, cell_list)


def include_cells(cells):
    """Apply inclusion rule to row.

    This means find which cells have a unique value.

    inclusion_list is a dict holding {val1: [col#, col#], val2: [col#]}
    """
    inclusion_list = {}
    for col, sub_cell in enumerate(cells):
        for value in sub_cell.values:
            if value not in inclusion_list:
                inclusion_list[value] = []
            inclusion_list[value] += [col]
    for num, qty in inclusion_list.items():
        if len(qty) == 1:
            cells[qty[0]].values = {num}


def fill_cells_include(board):
    """Use inclusion rule to fill cells."""
    board_transpose = [list(x) for x in zip(*board)]
    board_box = [board[i // ORDER][i % ORDER] for i in range(ORDER**2)]
    for i in range(ORDER**2):
        include_cells(board[i])
        include_cells(board_transpose[i])
        include_cells(board_box[i])


def fill_cells(board):
    """Fill cells."""
    fill_cells_exclude(board)
    fill_cells_include(board)


def main():
    board = make_blank_board()
    row_list, col_list, box_list, num_list = make_lists(board)
    add_filled_cells_from_file(row_list)
    display_board(row_list)
    count = ORDER ** 6
    post_iter_count = count_choices_left(board)
    count_filled = count_filled_cells(row_list)
    print('Starting with {} cells filled, {} choices left'
          .format(count_filled, post_iter_count))

    # while post_iter_count < count:
    #     fill_cells(board)
    #     count = post_iter_count
    #     post_iter_count = count_choices_left(board)
    #     count_filled = count_filled_cells(board)
    #     display_board(board)
    #     print('{} cells filled, {} choices left.'
    #           .format(count_filled, post_iter_count))
    #     print(board[-1][-1])


if __name__ == '__main__':
    main()
