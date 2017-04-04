#!/usr/bin/python3.4

#
#
# Luis Pena
# Jan 16, 2016
#
#This program prompts the user to input
# - The number of gallon of gas in the tank
# - The fuel efficiency in miles per gallon
# - The price of gas per gallon
#
#
# Purpose: Compute the cost per 100 miles and 
# how far the car can go with the gas in the tank. 
# Outputs: Print the cost per 100 miles and how far the can go with the gas in the tank. 
#
#

#Initialize Variables
gallonsOfGas = 0.0
fuelEffPerGallon = 0.0
gasPrice = 0.0
totalCostPerMiles = 0.0
totalMiles = 0.0

# Get Input from User
gallonsOfGas = float(input("Enter Number of gallons of gas in the tank: "))
fuelEffPerGallon = float(input("Enter The Fuel Efficiency in miles per gallon: "))
gasPrice = float(input("Enter Price of gas per gallon: "))


# Calculate Input from User
totalCostPerMiles = gasPrice * 100 / fuelEffPerGallon
print "For each 100 miles, total gas will cost "
print totalCostPerMiles, "Dollars"

totalMiles = gallonsOfGas * fuelEffPerGallon
print "The car can go "
print totalMiles, "Miles"
