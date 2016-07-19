"""
Individual Project to calculate the cost of painting a wall
Inputs:  Wall height, width and cost per gallon of painting
Output:  cost
Optional Output:  quantity of gallons of paint to buy
"""

#1. Setup
import math

GAL_PER_SQ_FT = 400  # Gallons per square foot

def get_num_walls():
    """ Prompt and ask user for number of walls to paint. """
    return int(input('How many walls do you want to paint? '))


def get_wall_area(i):
    """ Prompt user for height and width, return area of wall. """
    print('What is the width of the wall ' + str(i + 1) + ' (feet)? ', end = '')
    width_feet = float(input())
    print('What is the height of the wall ' + str(i + 1) + '(feet)? ', end = '')
    height_feet = float(input())
    return width_feet * height_feet


def get_price_gallon():
    """ Ask user for price per gallon of paint. """
    return float(input('How much does a gallon of paint cost (dollars)? '))


def get_num_coats():
    """ Ask user for number of coats of paint. """
    return int(input('How many coats do you want to apply? '))


def calc_used_gallons(num, area):
    """ Calculate how many gallons are needed. """
    return num * area / GAL_PER_SQ_FT


def calc_num_gallons(num):
    """ Round up gallons to avoid partial cans. """
    return math.ceil(num)


def out_cost_dollars(num, price):
    """ Print price. """
    cost_dollars = round(num * price, 2)
    print('It will cost you ${:.2f}'.format(cost_dollars))


def main():
    sum_area_sqft = 0
    num_walls = get_num_walls()
    for i in range(num_walls):
        wall_area = get_wall_area(i)
        sum_area_sqft += wall_area
    price_gallon = get_price_gallon()
    num_coats = get_num_coats()
    num_used_gallons = calc_used_gallons(num_coats, sum_area_sqft)
    num_gallons = calc_num_gallons(num_used_gallons)
    out_cost_dollars(num_gallons, price_gallon)


main()
