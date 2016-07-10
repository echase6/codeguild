"""
This program calculates Oregon income tax using the 2014 tax brackets.
This version relies on a list of tax brackets in tuples of the form
  (income level, taxation rate) and assumming that they are in order.

This is an individual project by Eric Chase, 7/9/16

Input:  income
Output:  Oregon income tax
"""

# 1. Setup
tax_burden = 0.0
brackets = [
    (3350, 0.05),
    (5050, 0.07),
    (116600, 0.09),
    (None, 0.099)
]

# 2. Input
print('I will calculate your Oregon Income Tax.')
taxable_income = float(input('Please tell me how much income you earned: '))

# 3. Transform
tax_rate_previous = 0
tax_burden = 0
for income_step, tax_rate in brackets:
    if taxable_income > 0:
#        income_step, tax_rate = bracket
        tax_burden += taxable_income * (tax_rate - tax_rate_previous)
        tax_rate_previous = tax_rate
        if income_step != None:
            taxable_income -= income_step

# 4. Output
print('Your tax burden is ${:.2f}'.format(round(tax_burden, 2)))
