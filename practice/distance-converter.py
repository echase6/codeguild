"""

"""
MILE_METER = 1609.344
KM_METER = 1000
FT_METER = 0.3048
IN_METER = 0.0254
CM_METER = 0.01
GAL_LI = 3.78541

unit1 = input('What is the units you are using' +
              '(mi, km, ft, m, in, cm, or li, gal,)? ')
amount = float(input('How many? '))
unit2 = input('What is the units you are converting to' +
              '(mi, km, ft, m, in, cm, or li, gal)? ')


if (unit1 == 'li' and unit2 != 'gal') or (unit1 == 'gal' and unit2 != 'li'):
    print('error Will Robinson')
elif (unit2 == 'li' and unit1 != 'gal') or (unit2 == 'gal' and unit1 != 'li'):
    print('error can not convert area and length')
else:
    if unit1 == 'mi':
        converted = amount * MILE_METER
    elif unit1 == 'km':
        converted = amount * KM_METER
    elif unit1 == 'ft':
        converted = amount * FT_METER
    elif unit1 == 'in':
        converted = amount * IN_METER
    elif unit1 == 'cm':
        converted = amount * CM_METER
    elif unit1 == 'gal':
        converted = amount * GAL_LI
    else:
        converted = amount
    if unit2 == 'mi':
        final = converted / MILE_METER
    elif unit2 == 'km':
        final = converted / KM_METER
    elif unit2 == 'ft':
        final = converted / FT_METER
    elif unit2 == 'in':
        final = converted / IN_METER
    elif unit2 == 'cm':
        final = converted / CM_METER
    elif unit2 == 'gal':
        final = converted / GAL_LI

    else:
        final = converted

    print('Your converted unit is ', final, ' ', unit2)
