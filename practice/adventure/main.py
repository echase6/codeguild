from creature import Creature
from weapon import Weapon
from potion import Potion


def make_entities():
    """Create and return list of all entities, to start game."""
    entities = [
                Creature((5, 5), 10, [], '*'),
                Creature((9, 5), 1, [], '@'),
                Creature((5, 9), 1, [], '@'),
                Potion((1, 2), 8, '#'),
                Weapon((2, 4), 5, '/'),
                Weapon((7, 1), 6, '(')
                ]
    return entities


def render_board(board):
    """Display board with entities.

    """
    for line in board:
        print(' '.join(line))


def initialize_board(entities):
    board = []
    for i in range(10):
        board += [['.'] * 10]
    for entity in entities:
        board[entity.location[0]][entity.location[1]] = entity.icon
    return board


def get_user_move(board, entities):
    """Ask the user for his move and make appropriate changes."""
    return False


def main():
    entities = make_entities()
    board = initialize_board(entities)
    game_on = True
    while game_on:
        game_on = get_user_move(board, entities)
        render_board(board)


if __name__ == '__main__':
    main()
