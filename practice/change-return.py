# 1. Setup
FRANKLIN = 10000
GRANT = 5000
JACKSON = 2000
HAMILTON = 1000
LINCOLN = 500
WASHINGTON = 100
QUARTER = 25
DIME = 10
NICKEL = 5

# 2. Input
print('How much change do you want me to dispense?')
change_remaining = float(input())


# 3. Transform
change_remaining *= 100
change_remaining = int(change_remaining)

num_franklins = change_remaining // FRANKLIN
change_remaining -= num_franklins * FRANKLIN
num_grants = change_remaining // GRANT
change_remaining -= num_grants * GRANT
num_jacksons = change_remaining // JACKSON
change_remaining -= num_jacksons * JACKSON
num_hamiltons = change_remaining // HAMILTON
change_remaining -= num_hamiltons * HAMILTON
num_lincolns = change_remaining // LINCOLN
change_remaining -= num_lincolns * LINCOLN
num_washingtons = change_remaining // WASHINGTON
change_remaining -= num_washingtons * WASHINGTON
num_quarters = change_remaining // QUARTER
change_remaining -= num_quarters * QUARTER
num_dimes = change_remaining // DIME
change_remaining -= num_dimes * DIME
num_nickels = change_remaining // NICKEL
change_remaining -= num_nickels * NICKEL

#4. Output
print('I will dispense:')
print(str(num_franklins) + ' hundred dollar bills')
print(str(num_grants) + ' fifty dollar bills')
print(str(num_jacksons) + ' twenty dollar bills')
print(str(num_hamiltons) + ' ten dollar bills')
print(str(num_lincolns) + ' five dollar bills')
print(str(num_washingtons) + ' one dollar bills')
print(str(num_quarters) + ' quarters')
print(str(num_dimes) + ' dimes')
print(str(num_nickels) + ' nickels')
print(str(change_remaining) + ' pennies')
