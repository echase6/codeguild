"""
Distance conversion program, that converts a quantity between two different
units.  Alternatively, it converts between gallons and liters.
This is the product of a collaboration between Andrew Champion, Jason Lingel
and Eric Chase

Inputs:  Quantity with units, and units to convert to
Output:  Quantity in the desired units
"""

NORM = {
    'Em': 1000000000000000000,
    'Pm': 1000000000000000,
    'Tm': 1000000000000,
    'Gm': 1000000000,
    'Mm': 1000000,
    'km': 1000,
    'hm': 100,
    'dam': 10,
    'm': 1,
    'dm': 0.1,
    'cm': 0.01,
    'mm': 0.001,
    'um': 0.000001,
    'nm': 0.000000001,
    'pm': 0.000000000001,
    'fm': 0.000000000000001,
    'am': 0.000000000000000001,
    'ft': 0.3048,
    'in': 0.0254,
    'gal': 3.78541,
    'li': 1,
    'l': 1,
    'mi': 1609.34,
}

valid_units = str(NORM.keys())
print('Valid units: ' + valid_units)

unit_in = input('What is the units you are using? ')

amount = float(input('How many? '))
unit_out = input('What is the units you are converting to? ')

if (
    (unit_in == 'li' and unit_out != 'gal') or
    (unit_in == 'gal' and unit_out != 'li') or
    (unit_out == 'li' and unit_in != 'gal') or
    (unit_out == 'gal' and unit_in != 'li')
   ):
    print('error can not convert area and length')

else:
    converted = amount * NORM[unit_in]
    final = converted / NORM[unit_out]

    print('Your converted unit is ', final, ' ', unit_out)
