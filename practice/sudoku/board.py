from cell import Cell
from operator import attrgetter

INITIAL_SET = {
    4: {'0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'},
    3: {'1', '2', '3', '4', '5', '6', '7', '8', '9'},
    2: {'1', '2', '3', '4'}}
TEST_BOARD_FILES = {
    4: 'sudoku4.txt',
    3: 'sudoku3.txt',
    2: 'sudoku2.txt'
}
ORDER = 2


def make_blank_board():
    """Create and un-filled board.

    >>> ORDER = 2
    >>> make_blank_board()  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [Cell(row: 0, col: 0, box: 0, num: 0, filled: True),
    Cell(row: 0, col: 0, box: 0, num: 1, filled: True),
    ...
    Cell(row: 3, col: 3, box: 3, num: 3, filled: True)]
    """
    board = []
    for i in range(ORDER ** 2):
        for j in range(ORDER ** 2):
            b = i % ORDER + (j // ORDER) * ORDER
            for k in range(ORDER ** 2):
                cell = Cell(i, j, b, k, True)
                board.append(cell)
    return board


def get_cell_list(board, selector, value, by_selector):
    """Cell getter, based on row, col, num.

    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> get_cell_list(board, 'num', 2, 'row')
    ...  # doctest: +NORMALIZE_WHITESPACE
    [[Cell(row: 0, col: 0, box: 1, num: 2, filled: True),
    Cell(row: 0, col: 1, box: 1, num: 2, filled: True),
    Cell(row: 0, col: 2, box: 1, num: 2, filled: True),
    Cell(row: 0, col: 3, box: 1, num: 2, filled: True)],
    [Cell(row: 1, col: 0, box: 1, num: 2, filled: True),
    Cell(row: 1, col: 1, box: 1, num: 2, filled: True),
    Cell(row: 1, col: 2, box: 1, num: 2, filled: True),
    Cell(row: 1, col: 3, box: 1, num: 2, filled: True)],
    [Cell(row: 2, col: 0, box: 3, num: 2, filled: True),
    Cell(row: 2, col: 1, box: 3, num: 2, filled: True),
    Cell(row: 2, col: 2, box: 3, num: 2, filled: False),
    Cell(row: 2, col: 3, box: 3, num: 2, filled: True)],
    [Cell(row: 3, col: 0, box: 3, num: 2, filled: True),
    Cell(row: 3, col: 1, box: 3, num: 2, filled: True),
    Cell(row: 3, col: 2, box: 3, num: 2, filled: True),
    Cell(row: 3, col: 3, box: 3, num: 2, filled: True)]]
    """
    cell_list = []
    selector_getter = attrgetter(selector)
    by_selector_getter = attrgetter(by_selector)
    for i in range(ORDER ** 2):
        cell_list += [[cell for cell in board
                       if selector_getter(cell) == value and
                       by_selector_getter(cell) == i]]
    return cell_list


def make_lists(board):
    """Populate lists."""
    row_list = []
    col_list = []
    box_list = []
    num_list = []
    for i in range(ORDER ** 2):
        row_list += [get_cell_list(board, 'row', i, 'col')]
        col_list += [get_cell_list(board, 'col', i, 'row')]
        box_list += [get_cell_list(board, 'box', i, 'row')]
        num_list += [get_cell_list(board, 'num', i, 'row')]
    return row_list, col_list, box_list, num_list


def deplete_cells(row_list, col_list, box_list, num_list):
    """Cell depleter, for testing purposes.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> deplete_cells(row_list, col_list, box_list, num_list)
    >>> num_list  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [[[Cell(row: 0, col: 0, box: 0, num: 0, filled: False),
    Cell(row: 0, col: 1, box: 0, num: 0, filled: True),
    Cell(row: 0, col: 2, box: 0, num: 0, filled: True),
    Cell(row: 0, col: 3, box: 0, num: 0, filled: True)],
    [Cell(row: 1, col: 0, box: 0, num: 0, filled: True),
    ...
    Cell(row: 3, col: 2, box: 3, num: 3, filled: True),
    Cell(row: 3, col: 3, box: 3, num: 3, filled: False)]]]
    """
    for i in range(ORDER ** 2):
        row_list[i][i][i].filled = False
        col_list[i][i][i].filled = False
        box_list[i][i][i].filled = False
        num_list[i][i][i].filled = False


def get_box_char(cell_list):
    r"""Return string representation of one cell in the board.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> get_box_char([Cell(2, 2, 2, 0, False), Cell(2, 2, 2, 1, False),
    ... Cell(2, 2, 3, 2, False), Cell(2, 2, 3, 3, True)])
    '3 '
    >>> get_box_char([Cell(2, 3, 2, 0, True), Cell(2, 3, 2, 1, True),
    ... Cell(2, 3, 3, 2, True), Cell(2, 3, 3, 3, True)])
    '. '
    """
    filled_list = [i for i in range(ORDER ** 2) if cell_list[i].filled]
    if len(filled_list) == 1:
        output_string = str(filled_list[0])
    else:
        output_string = '.'
    return output_string + ' '


def display_board(row_list):
    """Display the board, with filled-in squares.

    >>> ORDER = 2
    >>> from test_board_loader import test_board_loader
    >>> board = test_board_loader()
    >>> row_list, col_list, box_list, num_list = make_lists(board)
    >>> display_board(row_list)
    +-----+-----+
    | . . | . . |
    | . . | . . |
    +-----+-----+
    | . . | 3 . |
    | . . | . . |
    +-----+-----+

    """
    border_string = ('+' + '-' * (ORDER * 2 + 1)) * ORDER + '+'
    for row_index, row in enumerate(row_list):
        if row_index % ORDER == 0:
            print(border_string)
        line_string = ''
        for col_index, cell_list in enumerate(row):
            if col_index % ORDER == 0:
                line_string += '| '
            line_string += get_box_char(cell_list)
        print(line_string + '|')
    print(border_string)


def add_filled_cells_from_file(board):
    """Load the filled-in cells from a file."""
    file = TEST_BOARD_FILES[ORDER]
    with open(file) as f:
        contents = f.readlines()
    for i, line in enumerate(contents):
        line_char = list(line.strip())
        for j in range(ORDER ** 2):
            if line_char[j] != '.':
                board[i][j].values = {str(line_char[j])}
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
