"""
This program calculates Oregon income tax using the 2014 tax brackets.
This version relies on a list of tax brackets in tuples of the form
  (income level, taxation rate) and assumming that they are in order.

This is an individual project by Eric Chase, 7/9/16
Refactored to use functions 7/12/16

Input:  income
Output:  Oregon income tax
"""

# 1. Setup
BRACKETS = [
    (3350, 0.05),
    (5050, 0.07),
    (116600, 0.09),
    (None, 0.099)
]

def get_income():
    """ Get user input after prompting them.  """
    print('I will calculate your Oregon Income Tax.')
    return float(input('Please tell me how much income you earned: '))


def get_tax_burden(taxable_income):
    """ Calculate tax burden. """
    tax_rate_previous = 0
    tax_burden = 0.0
    for income_step, tax_rate in BRACKETS:
        if taxable_income > 0:
            tax_burden += taxable_income * (tax_rate - tax_rate_previous)
            tax_rate_previous = tax_rate
            if income_step != None:
                taxable_income -= income_step
    return tax_burden


def main():
    taxable_income = get_income()
    tax_burden = get_tax_burden(taxable_income)
    print('Your tax burden is ${:.2f}'.format(round(tax_burden, 2)))


main()
