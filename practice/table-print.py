"""Pretty table print.

Reads a file, and prints a pretty table.
"""
import csv
import sys


def get_filename():
    """Grab filename from command line argument."""
    filename = sys.argv[1]
    return filename


def get_table_line_lists(filename):
    """Read file into list of lines."""
    lines = []
    with open(filename, newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            lines += [row]
    return lines


def get_column_widths(cells):
    """Return list of the maximum width for each column index.

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
    """Create output string for one row."""
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
    filename = get_filename()
    row_contents = get_table_line_lists(filename)
    column_widths = get_column_widths(row_contents)
    output_table(column_widths, row_contents)


if __name__ == '__main__':
    main()
