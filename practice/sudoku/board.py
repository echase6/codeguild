from cell import Cell

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
    >>> make_blank_board()  # doctest: +NORMALIZE_WHITESPACE
    [
    [Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4})],
    [Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4})],
    [Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4})],
    [Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4}),Cell({1, 2, 3, 4})]
    ]
    """
    board = []
    for i in range(ORDER ** 2):
        board += [[Cell(INITIAL_SET[ORDER], i, j) for j in range(ORDER ** 2)]]
    return board


def add_filled_cells(board):
    """Add a few filled-in cells."""
    for i in range(1, ORDER ** 2):
        board[i][i].values = {i}
    return board


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
