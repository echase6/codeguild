"""
Individual Project to calculate the cost of painting a wall
Inputs:  Wall height, width and cost per gallon of painting
Output:  cost
Optional Output:  quantity of gallons of paint to buy
"""

#1. Setup
import math
GAL_PER_SQ_FT = 400  # Gallons per square foot
sum_area_sqft = 0

#2. Input
print('Let me calculate how much your painting project will cost.')
num_walls = int(input('How many walls do you want to paint? '))
for i in range(num_walls):
    print('What is the width of the wall ' + str(i) + ' (feet)?')
    width_feet = float(input())
    print('What is the height of the wall ' + str(i) + '(feet)?')
    height_feet = float(input())
    sum_area_sqft += width_feet * height_feet
price_gallon = float(input('How much does a gallon of paint cost (dollars)?'))
num_coats = int(input('How many coats do you want to apply?'))

#3. Transform
num_used_gallons = num_coats * sum_area_sqft / GAL_PER_SQ_FT
num_gallons = math.ceil(num_used_gallons)
cost_dollars = int(num_gallons * price_gallon * 100) / 100

#4. Output
print('You will use ' + str(num_used_gallons) + ' gallons of paint.')
print('You should buy ' + str(num_gallons) + ' gallons of paint.')
print('It will cost you $' + str(cost_dollars))
