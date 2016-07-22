"""Play the connect four game.

This program accomplishes the following:
  Read moves file from connect-four-moves.txt, which is alternating moves
  Makes each move on the board and displays the board after each move
  Alternates the player after each move automatically
  Analyzes the board for a sequence of four in rows, columns, or diagonally
  Prints out whomever won, if anyone.
"""

PLAYERS = ['R', 'Y']


def board_with_move(player_num, move, board):
    """Add move to board.

    >>> board_with_move(0, 2, [['R', 'Y'], ['Y', 'R', 'Y'], [], [], [], [], []])
    [['R', 'Y'], ['Y', 'R', 'Y'], ['R'], [], [], [], []]
    """
    board[move].append(PLAYERS[player_num])
    return board


def height_of_tallest_column(board):
    """Return the height of the tallest column in the board.

    >>> height_of_tallest_column([['R', 'Y'], ['Y', 'R', 'Y']])
    3
    """
    return max([len(col) for col in board])


def output_board(board):
    """Display the board.

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
    """Get moves from a file, add to the board, show board after each move."""
    board = [[], [], [], [], [], [], []]
    player_num = 0
    filename = 'connect-four-moves.txt'
    with open(filename) as f:
        for move in f:
            move = int(move) - 1  # the file is 1-based
            print('Player {}: Move: {}'.format(PLAYERS[player_num], str(move)))
            board = board_with_move(player_num, move, board)
            output_board(board)
            # input('Press key to continue...')
            player_num = (player_num + 1) % len(PLAYERS)
    return board


def make_square_board(board):
    """Fill the empty items to make the board rectangular.

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
    >>> check_horizontal([['Y', 'Y'], ['R', ''], ['Y', ''], ['R', ''],
    ...                   ['R', ''], ['', ''], ['', '']])
    []

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
    >>> check_vertical([['Y', 'Y', 'R', 'Y', 'R' ], ['R', 'R'],
    ...                 ['R'], ['R'], ['R'], [], []])
    []

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
    """ check for positive diagonal in smaller chunk.
    >>> check_4x4_diag([['Y', 'Y', 'R', 'Y'], ['R', 'Y', 'Y', ''],
    ...                 ['R', 'R', 'Y', ''], ['R', 'Y', 'R', 'Y']], 'Y')
    True
    >>> check_4x4_diag([['Y', 'Y', 'R', 'Y'], ['R', 'R', 'Y', ''],
    ...                 ['R', 'R', 'Y', ''], ['R', 'Y', 'R', 'Y']], 'Y')
    False

    """
    return [chunk[i][i] for i in range(4)] == [player] * 4


def check_diagonal(board):
    """

    >>> check_diagonal([['Y', 'Y', 'Y', '', ''], ['R', 'R', '', '', ''],
    ...                 ['Y', 'Y', 'R', 'Y', 'R'], ['R', 'R', '', '', ''],
    ...                 ['Y', 'Y', 'R', 'Y', ''], ['R', 'R', 'Y', 'R', ''],
    ...                 ['Y', 'Y', 'Y', 'Y', 'R']])
    ['R']
    """
    matches = []
    height = len(board[0])
    for col_num in range(4):
        for row_num in range(height - 3):
            for player in PLAYERS:
                chunk = ([col[row_num: row_num + 4]
                          for col in board[col_num: col_num + 4]])
                if check_4x4_diag(chunk, player):
                    matches += player
                if check_4x4_diag(list(reversed(chunk)), player):
                    matches += player
    return matches


def find_who_won(board):
    """Return the winner(s), if any."""
    winners = set()
    board = make_square_board(board)
    winners.update(check_horizontal(board))
    winners.update(check_vertical(board))
    winners.update(check_diagonal(board))
    return winners


def output_who_won(winners):
    """Print the winning results.

    >>> output_who_won({'R', 'Y'})
    Everybody is a winner!
    >>> output_who_won({})
    Nobody won.
    >>> output_who_won({'Y'})
    Y is a winner.
    """
    if len(winners) == 0:
        print('Nobody won.')
    elif len(winners) == len(PLAYERS):
        print('Everybody is a winner!')
    else:
        for winner in winners:
            print('{} is a winner.'.format(winner))


def main():
    board = get_moves()
    winners = find_who_won(board)
    output_who_won(winners)


if __name__ == '__main__':
    main()
