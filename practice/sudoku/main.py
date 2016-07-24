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


def fill_cells_exclude(board):
    """Use exclusionary rule to fill cells."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            exclude_cell_row(i, j, cell, board)
            exclude_cell_col(i, j, cell, board)
            exclude_cell_box(i, j, cell, board)


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


def fill_cells_include(board):
    """Use inclusion rule to fill cells."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            include_row(i, board)
            include_col(j, board)
            # include_box(i, j, board)


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
