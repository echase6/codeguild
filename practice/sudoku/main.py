from cell import Cell


INITIAL_SET = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def make_blank_board():
    """Create and un-filled board."""
    board = []
    for i in range(9):
        board += [[Cell((7, 7), INITIAL_SET) for i in range(9)]]
    return board


def add_filled_cells(board):
    """Add a few filled-in cells."""
    for i in range(1, 9):
        board[i][i].values = {i}
    return board


def add_filled_cells_from_file(board):
    """Load the filled-in cells from a file."""
    file = 'sudoku.txt'
    with open(file) as f:
        contents = f.readlines()
    for i, line in enumerate(contents):
        line_char = list(line.strip())
        for j in range(9):
            if line_char[j] != '.':
                board[i][j].values = {int(line_char[j])}
    return board


def count_filled_cells(board):
    """Return the number of filled cells."""
    count = 0
    for row in board:
        count += sum([1 for cell in row if len(cell.values) == 1])
    return count


def count_choices_left(board):
    """Return the number of choices left."""
    count = 0
    for row in board:
        count += sum([len(cell.values) for cell in row])
    return count


def get_three_char(cells):
    """Return string representation of three cells.


    """
    output_string = ''
    for cell in cells:
        if len(cell.values) == 1:
            output_string += str(list(cell.values)[0])
        else:
            output_string += '.'
        output_string += ' '
    return output_string[0:5]


def display_board(board):
    """Display the board, with filled-in squares."""
    border_string = ('+' + '-' * 5) * 3 + '+'
    print(border_string)
    for i in range(3):
        for j in range(3):
            line_string = ('|' + get_three_char(board[i * 3 + j][0:3]) + '|' +
                           get_three_char(board[i * 3 + j][3:6]) + '|' +
                           get_three_char(board[i * 3 + j][6:9]) + '|'
                           )
            print(line_string)
        print(border_string)


def exclude_cell_row(i, j, cell, board):
    """Apply exclusionary rule to cell in row."""
    row = board[i]
    for col, sub_cell in enumerate(row):
        if col != j and len(sub_cell.values) == 1:
            cell.values = cell.values.difference(sub_cell.values)
            # print(cell.values, sub_cell.values)


def exclude_cell_col(i, j, cell, board):
    """Apply exclusionary rule to cell in column."""
    board_transpose = [list(x) for x in zip(*board)]
    exclude_cell_row(j, i, cell, board_transpose)


def exclude_cell_box(i_index, j_index, cell, board):
    """Apply exclusionary rule to cell in box."""
    box_row = i_index // 3
    sub_row = i_index % 3
    box_col = j_index // 3
    sub_col = j_index % 3
    for i, row in enumerate(board[box_row*3:box_row*3+3]):
        for j, sub_cell in enumerate(row[box_col*3:box_col*3+3]):
            if not(i == sub_row and j == sub_col) and len(sub_cell.values) == 1:
                cell.values = cell.values.difference(sub_cell.values)


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
    box_row = i_index // 3
    sub_row = i_index % 3
    box_col = j_index // 3
    sub_col = j_index % 3
    value_pair = cell.values
    for i, row in enumerate(board[box_row*3:box_row*3+3]):
        for j, sub_cell in enumerate(row[box_col*3:box_col*3+3]):
            if not(sub_row == i and sub_col == j) and sub_cell.values == value_pair:
                for sub_row2, row2 in enumerate(board[box_row * 3:box_row * 3 + 3]):
                    for sub_col2, cell2 in enumerate(row2[box_col * 3:box_col * 3 + 3]):
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
            exclude_cell_row(i, j, cell, board)
            exclude_cell_col(i, j, cell, board)
            exclude_cell_box(i, j, cell, board)
            exclude_cell_pairs_row(i, j, cell, board)
            exclude_cell_pairs_col(i, j, cell, board)
            exclude_cell_pairs_box(i, j, cell, board)


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
    for box_row, row in enumerate(board[i*3:i*3+3]):
        for box_col, sub_cell in enumerate(row[j*3:j*3+3]):
            for value in sub_cell.values:
                if value not in inclusion_list:
                    inclusion_list[value] = []
                inclusion_list[value] += [(box_row, box_col)]
    for num, qty in inclusion_list.items():
        if len(qty) == 1:
            row, col = qty[0]
            board[i*3+row][j*3+col].values = {num}


def fill_cells_include(board):
    """Use inclusion rule to fill cells."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            include_row(i, board)
            include_col(j, board)
    for i in range(len(board) // 3):
        for j in range(len(board[i]) // 3):
            include_box(i, j, board)


def fill_cells(board):
    """Fill cells."""
    fill_cells_exclude(board)
    fill_cells_include(board)


def main():
    board = make_blank_board()
    board = add_filled_cells_from_file(board)
    display_board(board)
    count = pow(9, 3)
    post_iter_count = count_choices_left(board)
    count_filled = count_filled_cells(board)
    print('Starting with {} cells filled, {} choices left'
          .format(count_filled, post_iter_count))
    while post_iter_count < count:
        fill_cells(board)
        count = post_iter_count
        post_iter_count = count_choices_left(board)
        count_filled = count_filled_cells(board)
        display_board(board)
        print('{} cells filled, {} choices left.'
              .format(count_filled, post_iter_count))
        print(board[8][8])


if __name__ == '__main__':
    main()
