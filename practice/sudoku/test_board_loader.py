from cell import Cell


def test_board_loader():
    """  """
    board = ([
    Cell(0, 0, 0, 0, True), Cell(0, 0, 0, 1, True), Cell(0, 0, 0, 2, True), Cell(0, 0, 0, 3, True),
    Cell(0, 1, 0, 0, True), Cell(0, 1, 0, 1, True), Cell(0, 1, 0, 2, True), Cell(0, 1, 0, 3, True),
    Cell(0, 2, 1, 0, True), Cell(0, 2, 1, 1, True), Cell(0, 2, 1, 2, True), Cell(0, 2, 1, 3, True),
    Cell(0, 3, 1, 0, True), Cell(0, 3, 1, 1, True), Cell(0, 3, 1, 2, True), Cell(0, 3, 1, 3, True),
    Cell(1, 0, 0, 0, True), Cell(1, 0, 0, 1, True), Cell(1, 0, 0, 2, True), Cell(1, 0, 0, 3, True),
    Cell(1, 1, 0, 0, True), Cell(1, 1, 0, 1, True), Cell(1, 1, 0, 2, True), Cell(1, 1, 0, 3, True),
    Cell(1, 2, 1, 0, True), Cell(1, 2, 1, 1, True), Cell(1, 2, 1, 2, True), Cell(1, 2, 1, 3, True),
    Cell(1, 3, 1, 0, True), Cell(1, 3, 1, 1, True), Cell(1, 3, 1, 2, True), Cell(1, 3, 1, 3, True),
    Cell(2, 0, 2, 0, True), Cell(2, 0, 2, 1, True), Cell(2, 0, 2, 2, True), Cell(2, 0, 2, 3, True),
    Cell(2, 1, 2, 0, True), Cell(2, 1, 2, 1, True), Cell(2, 1, 2, 2, True), Cell(2, 1, 2, 3, True),
    Cell(2, 2, 3, 0, False), Cell(2, 2, 3, 1, False), Cell(2, 2, 3, 2, False), Cell(2, 2, 3, 3, True),
    Cell(2, 3, 3, 0, True), Cell(2, 3, 3, 1, True), Cell(2, 3, 3, 2, True), Cell(2, 3, 3, 3, True),
    Cell(3, 0, 2, 0, True), Cell(3, 0, 2, 1, True), Cell(3, 0, 2, 2, True), Cell(3, 0, 2, 3, True),
    Cell(3, 1, 2, 0, True), Cell(3, 1, 2, 1, True), Cell(3, 1, 2, 2, True), Cell(3, 1, 2, 3, True),
    Cell(3, 2, 3, 0, True), Cell(3, 2, 3, 1, True), Cell(3, 2, 3, 2, True), Cell(3, 2, 3, 3, True),
    Cell(3, 3, 3, 0, True), Cell(3, 3, 3, 1, True), Cell(3, 3, 3, 2, True), Cell(3, 3, 3, 3, True),
    ])
    return board