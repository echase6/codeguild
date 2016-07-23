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


def main():
    board = make_blank_board()
    board = add_filled_cells_from_file(board)
    display_board(board)


if __name__ == '__main__':
    main()


