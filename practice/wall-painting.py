"""
Individual Project to calculate the cost of painting a wall
Inputs:  Wall height, width and cost per gallon of painting
Output:  cost
Optional Output:  quantity of gallons of paint to buy
"""

#1. Setup
import math
COVERS = 400  # Gallons per square foot

#2. Input
print('Let me calculate how much your painting project will cost.')
print('What is the width of the wall?')
width = float(input())
print('What is the height of the wall?')
height = float(input())
print('How much does a gallon of paint cost?')
price_gallon = float(input())

#3. Transform
num_used_gallons = width * height / COVERS
num_gallons = math.ceil(num_used_gallons)
cost = int(num_gallons * price_gallon * 100) / 100

#4. Output
print('You will use ' + str(num_used_gallons) + ' gallons of paint.')
print('You should buy ' + str(num_gallons) + ' gallons of paint.')
print('It will cost you $' + str(cost))
