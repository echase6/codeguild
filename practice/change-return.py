
"""
Change return program to convert between an amount of money to quantities
of common denominations of currency and coins.
This is the product of a collaborative effort between Corey Adkins,
Andrew Champion and Eric Chase
Refactored to use functions 7/12/16

Input:  Amount of money, in dollars
Output:  Amount of each demonition
"""

# 1. Setup
DENOMINATIONS = [
    ['hundred dollar bill', 10000],
    ['fifty dollar bill', 5000],
    ['twenty dollar bill', 2000],
    ['ten dollar bill', 1000],
    ['five dollar bill', 500],
    ['two dollar bill', 200],ls
    ['one dollar bill', 100],
    ['quarter', 25],
    ['dime', 10],
    ['nickel', 5],
    ['penny', 1]]


def get_user_input():
    """ Learn how much change needs to be converted. """
    dollars = float(input('How much change do you want me to dispense? '))
    return int(100 * dollars)

def calc_num_change_remaining(i, change_remaining):
    """ Returns number of each denomination and the remaining change. """
    num = change_remaining // DENOMINATIONS[i][1]
    change_remaining -= num * DENOMINATIONS[i][1]
    return num, change_remaining

def output_quantity(i, num):
    """ Print the quantity of each denomination, accounting for 0 and 1. """
    if num > 1:
        print('  {} {}s'.format(num, DENOMINATIONS[i][0]))
    elif num > 0:
        print('  {} {}'.format(num, DENOMINATIONS[i][0]))
    return

def main():
    change_remaining = get_user_input()
    print('I will dispense:')
    for i in range(len(DENOMINATIONS)):
        num, change_remaining = calc_num_change_remaining(i, change_remaining)
        output_quantity(i, num)

main()
