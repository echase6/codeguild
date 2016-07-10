"""
This program calculates Oregon income tax using the 2014 tax brackets.

This is an individual project by Eric Chase, 7/9/16

Input:  income
Output:  Oregon income tax
"""

# 1. Setup
tax_burden = 0.0

# 2. Input
print('I will calculate your Oregon Income Tax.')
taxable_income = float(input('Please tell me how much income you earned: '))

# 3. Transform
tax_burden += taxable_income * 0.05
taxable_income -= 3350.00
if taxable_income > 0:
    tax_burden += taxable_income * (0.07 - 0.05)
    taxable_income -= 5050.00
if taxable_income > 0:
    tax_burden += taxable_income * (0.09 - 0.07)
    taxable_income -= 116000.00
if taxable_income > 0:
    tax_burden += taxable_income * (0.099 - 0.09)

# 4. Output
print('Your tax burden is ${:.2f}'.format(round(tax_burden, 2)))
