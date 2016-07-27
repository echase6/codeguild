from cell import Cell
from board import make_blank_board, add_filled_cells_from_file
from board import count_choices_left, count_filled_cells
from board import ORDER


def get_box_char(cells):
    r"""Return string representation of one row in a box.

    >>> ORDER = 2
    >>> get_box_char([Cell({'2', '9'}), Cell({'4'})])
    '. 4'
    """
    output_string = ''
    for cell in cells:
        if len(cell.values) == 1:
            output_string += str(list(cell.values)[0])
        else:
            output_string += '.'
        output_string += ' '
    return output_string[0:ORDER * 2 - 1]


def display_board(board):
    """Display the board, with filled-in squares."""
    border_string = ('+' + '-' * (ORDER*2-1)) * ORDER + '+'
    print(border_string)
    for i in range(ORDER):
        for j in range(ORDER):
            board_row = board[i * ORDER + j]
            line_string = ''
            for k in range(0, ORDER**2, ORDER):
                line_string += get_box_char(board_row[k:k + ORDER]) + '|'
            print('|' + line_string)
        print(border_string)


def exclude_cell_row_col(i, j, cell, board):
    """Apply exclusionary rule to cell in row.

    >>> board = (
    ... [[Cell({'1'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})],
    ...  [Cell({'1', '2'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})],
    ...  [Cell({'2'}), Cell({'1', '3'}), Cell({'4'}), Cell({'3', '4'})],
    ...  [Cell({'4'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]])
    >>> exclude_cell_row_col(0, 0, Cell({'1'}), board)
    >>> board
    [[Cell({'1'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})], \
[Cell({'2'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})], \
[Cell({'2'}), Cell({'1', '3'}), Cell({'4'}), Cell({'3', '4'})], \
[Cell({'4'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]]
    """

    if len(cell.values) == 1:
        for idx in range(ORDER**2):
            if idx != i:
                board[idx][j].values = board[idx][j].values.difference(cell.values)
            if idx != j:
                # print(idx, i, j, [cell.values], [board[i][idx].values])
                board[i][idx].values = board[i][idx].values.difference(cell.values)

    # row = board[i]
    # for col, sub_cell in enumerate(row):
    #     if col != j and len(cell.values) == 1:
    #         sub_cell.values = sub_cell.values.difference(cell.values)
    #         # print(cell.values, sub_cell.values)


# def exclude_cell_col(i, j, cell, board):
#     """Apply exclusionary rule to cell in column.
#
#     >>> board = (
#     ... [[Cell({'1'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]])
#     >>> exclude_cell_row(0, 0, Cell({'1'}), board)
#     >>> board
#     [[Cell({'1'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})]
#     """
#     board_transpose = [list(x) for x in zip(*board)]
#     exclude_cell_row(j, i, cell, board_transpose)


def exclude_cell_box(i_index, j_index, cell, board):
    """Apply exclusionary rule to cell in box.

    >>> board = (
    ... [[Cell({'1'}), Cell({'2', '3'}), Cell({'3', '4'}), Cell({'3', '4'})],
    ...  [Cell({'1', '2'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})],
    ...  [Cell({'2'}), Cell({'1', '3'}), Cell({'4'}), Cell({'3', '4'})],
    ...  [Cell({'4'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]])
    >>> exclude_cell_box(0, 0, Cell({'1'}), board)
    >>> board
    [[Cell({'1'}), Cell({'2', '3'}), Cell({'3', '4'}), Cell({'3', '4'})],\
[Cell({'1', '2'}), Cell({'3'}), Cell({'3', '4'}), Cell({'3', '4'})],\
[Cell({'2'}), Cell({'1', '3'}), Cell({'4'}), Cell({'3', '4'})],\
[Cell({'4'}), Cell({'1', '3'}), Cell({'3', '4'}), Cell({'3', '4'})]])

    """
    box_row = i_index // ORDER
    sub_row = i_index % ORDER
    box_col = j_index // ORDER
    sub_col = j_index % ORDER
    if len(cell.values) == 1:
        return
    for i in range(ORDER):
        for j in range(ORDER):
            if not(i == sub_row and j == sub_col):
                sub_cell = board[box_row * ORDER + i][box_col * ORDER + j]
                sub_cell.values = sub_cell.values.difference(cell.values)


def exclude_cell_pairs_row(i, j, cell, board):
    """Apply exclusionary rule if two pairs exist in the row."""
    if len(cell.values) == 2:
        row = board[i]
        value_pair = cell.values
        for col, sub_cell in enumerate(row):
            if col != j and sub_cell.values == value_pair:
                for col2, cell2 in enumerate(row):
                    if col2 != col and col2 != j:
                        cell2.values = cell2.values.difference(value_pair)


def exclude_cell_pairs_col(i, j, cell, board):
    """Apply exclusionary rule if two pairs exist in the column."""
    board_transpose = [list(x) for x in zip(*board)]
    exclude_cell_pairs_row(j, i, cell, board_transpose)


def exclude_cell_pairs_box(i_index, j_index, cell, board):
    """Apply exclusionary rule if two pairs exist in the box."""
    box_row = i_index // ORDER
    sub_row = i_index % ORDER
    box_col = j_index // ORDER
    sub_col = j_index % ORDER
    value_pair = cell.values
    for i, row in enumerate(board[box_row*ORDER:(box_row+1)*ORDER]):
        for j, sub_cell in enumerate(row[box_col*ORDER:(box_col+1)*ORDER]):
            if not(sub_row == i and sub_col == j) and sub_cell.values == value_pair:
                for sub_row2, row2 in enumerate(board[box_row * ORDER:(box_row+1)*ORDER]):
                    for sub_col2, cell2 in enumerate(row2[box_col * ORDER:(box_col+1)*ORDER]):
                        if (not (sub_row == i and
                                sub_col == j and
                                sub_row2 == sub_row and
                                sub_col2 == sub_col)
                           and cell2.values == value_pair):
                                cell2.values = cell2.values.difference(value_pair)


def fill_cells_exclude(board):
    """Use exclusionary rule to fill cells."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            exclude_cell_row_col(i, j, cell, board)
            # exclude_cell_col(i, j, cell, board)
            # exclude_cell_box(i, j, cell, board)
            # exclude_cell_pairs_row(i, j, cell, board)
            # exclude_cell_pairs_col(i, j, cell, board)
            # exclude_cell_pairs_box(i, j, cell, board)


def include_row(i, board):
    """Apply inclusion rule to row."""
    inclusion_list = {}
    row = board[i]
    for col, sub_cell in enumerate(row):
        for value in sub_cell.values:
            if value not in inclusion_list:
                inclusion_list[value] = []
            inclusion_list[value] += [col]
    for num, qty in inclusion_list.items():
        if len(qty) == 1:
            board[i][qty[0]].values = {num}


def include_col(j, board):
    """Apply inclusion rule to column."""
    board_transpose = [list(x) for x in zip(*board)]
    include_row(j, board_transpose)


def include_box(i, j, board):
    """Apply inclusion rule to box."""
    inclusion_list = {}
    for box_row, row in enumerate(board[i*ORDER:(i+1)*ORDER]):
        for box_col, sub_cell in enumerate(row[j*ORDER:(j+1)*ORDER]):
            for value in sub_cell.values:
                if value not in inclusion_list:
                    inclusion_list[value] = []
                inclusion_list[value] += [(box_row, box_col)]
    for num, qty in inclusion_list.items():
        if len(qty) == 1:
            row, col = qty[0]
            board[i*ORDER+row][j*ORDER+col].values = {num}


def fill_cells_include(board):
    """Use inclusion rule to fill cells."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            include_row(i, board)
            include_col(j, board)
    for i in range(len(board) // ORDER):
        for j in range(len(board[i]) // ORDER):
            include_box(i, j, board)


def fill_cells(board):
    """Fill cells."""
    fill_cells_exclude(board)
    # fill_cells_include(board)


def main():
    board = make_blank_board()
    board = add_filled_cells_from_file(board)
    display_board(board)
    count = pow(ORDER, 6)
    post_iter_count = count_choices_left(board)
    count_filled = count_filled_cells(board)
    print('Starting with {} cells filled, {} choices left'
          .format(count_filled, post_iter_count))
    print(board[0][0])

    while post_iter_count < count:
        fill_cells(board)
        count = post_iter_count
        post_iter_count = count_choices_left(board)
        count_filled = count_filled_cells(board)
        display_board(board)
        print('{} cells filled, {} choices left.'
              .format(count_filled, post_iter_count))
        print(board[0][0])


if __name__ == '__main__':
    main()
