"""Play the connect four game."""

PLAYERS = ['R', 'Y']


def board_with_move(player_num, move, board):
    """Add move to board.

    >>> board_with_move(0, 2, [['R', 'Y'], ['Y', 'R', 'Y'], [], [], [], [], []])
    [['R', 'Y'], ['Y', 'R', 'Y'], ['R'], [], [], [], []]
    """
    board[move].append(PLAYERS[player_num])
    return board


def height_of_tallest_column(board):
    """Return the height of the tallest column.

    >>> height_of_tallest_column([['R', 'Y'], ['Y', 'R', 'Y']])
    3
    """
    return max([len(col) for col in board])


def output_board(board):
    """Display board

    >>> output_board([['R', 'Y'], ['Y', 'R', 'Y'], [], [], [], [], []])
    -Y-----
    YR-----
    RY-----
    """
    tallest = height_of_tallest_column(board)
    for i in range(tallest - 1, -1, -1):
        out_string = ''
        for col in range(7):
            if len(board[col]) > i:
                out_string += board[col][i]
            else:
                out_string += '-'
        print(out_string)


def get_moves():
    """Add the moves to the board, show result after each board."""
    board = [[], [], [], [], [], [], []]
    player_num = 0
    filename = 'connect-four-moves.txt'
    with open(filename) as f:
        for move in f:
            move = int(move) - 1
            print('Player {}: Move: {}'.format(PLAYERS[player_num], str(move)))
            board = board_with_move(player_num, move, board)
            output_board(board)
            # input('Press key to continue...')
            player_num = (player_num + 1) % len(PLAYERS)
    return board


def make_square_board(board):
    """Fill the empty items to make the board square.

    >>> make_square_board([['Y', 'Y', 'Y'], [''], ['R'], ['R'], ['R']])
    [['Y', 'Y', 'Y'], ['', '', ''], ['R', '', ''], ['R', '', ''], ['R', '', '']]
    """
    height = height_of_tallest_column(board)
    board = [item + [''] * (height - len(item)) for item in board]
    return board


def check_horizontal(board):
    """Check for a winner on the rows.

    >>> check_horizontal([['Y', 'Y'], ['R', ''], ['R', ''], ['R', ''],
    ...                   ['R', ''], ['', ''], ['', '']])
    ['R']

    """
    matches = []
    transposed_board = [list(x) for x in zip(*board)]
    for row in transposed_board:
        for start_col in range(4):
            for player in PLAYERS:
                if row[start_col: start_col + 4] == [player] * 4:
                    matches += player
    return matches


def check_vertical(board):
    """Check for a winner on the columns.

    >>> check_vertical([['Y', 'Y', 'Y', 'Y', 'R' ], ['R', 'R'],
    ...                 ['R'], ['R'], ['R'], [], []])
    ['Y']

    """
    matches = []
    height = len(board[0])
    for col in board:
        for start_row in range(height - 3):
            for player in PLAYERS:
                if col[start_row: start_row + 4] == [player] * 4:
                    matches += player
    return matches


def check_4x4_diag(chunk, player):
    """ check for diagonal in smaller chunk."""
    return [chunk[i][i] for i in range(4)] == [player] * 4


def check_diagonal(board):
    """  """
    matches = []
    height = len(board[0])
    for col in range(4):
        for row in range(height - 3):
            for player in PLAYERS:
                chunk = board[col: col + 4][row: row + 4]
                if check_4x4_diag(chunk, player):
                    matches += player
                if check_4x4_diag(list(reversed(chunk)), player):
                    matches += player
    return matches


def output_who_won(board):
    """Print the winner."""
    winners = set()
    board = make_square_board(board)
    winners.update(check_horizontal(board))
    winners.update(check_vertical(board))
    winners.update(check_diagonal(board))
    print(winners)
    return board


def main():
    board = get_moves()
    output_who_won(board)


if __name__ == '__main__':
    main()
