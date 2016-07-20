"""This is the goemetry problem."""

from point import Point
from rectangle import Rectangle
from math import sqrt


def set_point_values():
    """Set point values for testing."""
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    return point1, point2


def find_distance(point1, point2):
    """Find and return the distance between the two points.
    >>> find_distance(Point(1, 1), Point(4, 5))
    5.0
    """
    return sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))


def get_rewckt():
    """Set rectangle point and dimensions for testing."""
    return Rectangle(1.5, 3, 1, 1.5)


def find_if_inside(rect, point):
    """Test whether the point is inside the rectange.

    >>> find_if_inside(Rectangle(1.5, 3, 1, 1.5), Point(1, 1))
    False
    >>> find_if_inside(Rectangle(1.5, 3, 1, 1.5), Point(2, 2))
    True
    """
    return (point.x >= rect.x and
            point.x <= rect.x + rect.w and
            point.y <= rect.y and
            point.y >= rect.y - rect.h
            )


def find_rect_mid_point(rect):
    """Find and return the mid-point of the rectangle.

    >>> find_rect_mid_point(Rectangle(1, 3, 2, 2))
    Point(2.0, 2.0)
    """
    return Point(rect.x + rect.w/2, rect.y - rect.h/2)


def get_move_distance():
    """Return distances for the move operation."""
    return 1.0, 2.0


def find_moved_point(point, x_move, y_move):
    """Find and return a moved point.

    >>> find_moved_point(Point(1.0, 1.0), 1.0, 2.0)
    Point(2.0, 3.0)
    """
    return Point(point.x + x_move, point.y + y_move)


def main():
    point1, point2 = set_point_values()
    distance_between_points = find_distance(point1, point2)
    rect = get_rewckt()
    is_point_in_rectangle = find_if_inside(rect, point1)
    rect_mid_point = find_rect_mid_point(rect)
    x_move, y_move = get_move_distance()
    moved_point = find_moved_point(point1, x_move, y_move)
    print('The distance between the two points is {}'
          .format(distance_between_points))
    print('Is the point inside the rectangle? {}'.format(is_point_in_rectangle))
    print('The midpoint of the rectangle is {}'.format(rect_mid_point))
    print('The moved point is {}'.format(moved_point))


if __name__ == '__main__':
    main()
