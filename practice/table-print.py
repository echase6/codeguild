"""Pretty table print.

Reads a file, and prints a pretty table.
"""
# get user file name

filename = input('Please give me a text file so I can make you a pretty chart. ')

def get_table_lines(filename):
    """Read file into list of lines."""
    with open(filename) as f:
        lines = f.readlines()
    return lines


def split_into_cells(lines):
    """Split the lines into a list of cells.

    >>> split_into_cells(['Apple Gary', 'VW Portland'])
    [['Apple', 'Gary'], ['VW', 'Portland']]
    """
    cells = [x.strip().split(' ') for x in lines]
    return cells


def get_column_widths(cells):
    """Return list of the maximum width for each column index

    >>> get_column_widths([['Apple', 'Gary'], ['VW', 'Portland']])
    [5, 8]
    """
    max_widths = [0] * len(cells[0])
    for row in cells:
        # read each line
        for col, cell in enumerate(row):
            max_widths[col] = max(max_widths[col], len(cell))

    return max_widths


def make_output_line(widths, row):
    """Create output string for one row"""
    line_string = '|'
    for col, cell in enumerate(row):
        line_string += cell.ljust(widths[col], ' ') + '|'
    return line_string


def output_table(widths, cell_contents):
    """Prints the table, including top and bottom borders."""
    border = '|'
    for length in widths:
        border += '-' * length + '|'
    print(border)
    print(make_output_line(widths, cell_contents[0]))
    print(border)
    for row in cell_contents[1:]:
        print(make_output_line(widths, row))
    print(border)


def main():
    row_contents = get_table_lines(filename)
    cell_contents = split_into_cells(row_contents)
    column_widths = get_column_widths(cell_contents)
    output_table(column_widths, cell_contents)


if __name__ == '__main__':
    main()
