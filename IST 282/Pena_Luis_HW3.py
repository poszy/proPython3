#!/usr/bin/python3.4
# Author: Luis Pena
# Feb 6th, 2016
# Purpose: compute: the sum of all even numbers between
# a and b (inclusive), where a and b are inputs

# Delcare Variables
sum = 0


a = int(input("Enter A: " ))
b = int(input("Enter B: " ))


#Loop Logic
for i in range(a, b + 1):

    if( i % 2 == 0):
        sum = sum +i

    print(sum)

print("\n")
print("Last Number")
print(sum)
print("##### END PART A #####\n")
#
# Part B
#

print("##### BEGIN PART B ##### \n")
print ("Enter A series of Quiz Scores")
print("(Enter 0: to exit.)")

inputSum = 0
inputAverage = 0
inputCount = 0

while True:
    inputScore = int(input("Enter Score: "))
    if (inputScore ==0):
        print("Sum:     %10.2i"  %inputSum)
        print("Count:   %10.2i"  %inputCount)
        print("Average: %10.2i"  %inputAverage)

        break
    inputSum      = inputSum + inputScore
    inputCount    = inputCount + 1
    inputAverage  = inputSum // inputCount
