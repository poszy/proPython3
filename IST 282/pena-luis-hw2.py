#!/usr/bin/python3.4

# Homework 2
# Author : Luis M Pena
# Date: Jan 28 2016
# Purpose: Simple tax calculator with loops 

#Grab user input


income= float(input("Please Enter Your Income:"))
status  = input("Enter s for single, m for Married: ")



#print ("The income entered was \n", income)
#print ("The Status entered was \n", status)

if status == "s":
    print("You Selected the Single status:")
    
    if(income <= 32000):
        print(" With 10% applied, Total taxes are:")
        print (income * .10)

    else:
        print("With 25% applied, Total taxes are:")
        print ( income * .25)

else:
    print ("You selected a Married Status:")
      
    if(income <= 64000):
        print(" With 10% applied, Total taxes are:")
        print (income * .10)

    else:

        print(" With 25% applied, Total taxes are: ")
        print (income * .25)

