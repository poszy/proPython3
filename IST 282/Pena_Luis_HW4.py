# Luis Pena
# Homework 4
# Feb 29th 2016


import math 

def find_num_score(sList):
	return len(sList)

def find_sum(sList):
    total= sum(sList)
    return(total)

def find_average(num_score,sum):
    
    average = sum / num_score
    return average
	
def find_median(sList):
    sList.sort()
    length = len(sList)
    if length % 2 == 0:
        
        i = int(length/2)
        p = i - 1
        
        median = (sList[i]+sList[p])/2
        
        return median
    
    else:
        i = (length/2)
        i = int(i)
        median = sList[i]
        return median



def find_lowest(score):
	s = score
	lowest = s[0]
	index  = 1
	size   = len(s)
	
	while index < size:
		if s[index] < lowest:
			lowest = s[index]
		
		index = index +1 
		
	return lowest

def find_highest(score):
	s = score
	largest = s[0]
	index   = 1
	size    = len(s)
	
	while index < size:
		if s[index] > largest:
			
			largest = s[index]
		
		index = index +1 
		
	return largest
	
def find_stDev(sList,average):
	
	diff = (sList[0] - average)**2
	
	for i in range(1, len(sList)):
		diff += (average - sList[i])**2
		variance = diff/(len(sList) - 1)
		stDev = math.sqrt(variance)
		
	return stDev 
	
def main():
    sum       = 0
    num_score = 0 #number of midterm grades
    
    average  = 0.0
    lowest   = 0.0
    highest  = 0.0
    median   = 0.0
    score    = [98, 100, 68, 97, 72, 89, 99, 83, 75, 82, 87, 89, 81, 85, 93]

    # function calls/invocations
    num_score = find_num_score(score) #call by reference

    sum = find_sum(score)

    average = find_average(num_score,sum) # call by value 
    
    median = find_median (score)

    lowest = find_lowest (score)
    
    highest = find_highest (score)

    stDev = find_stDev(score, average)  
    print (" *********** Display the computation result ***********")

    print ("The number of scores: ", num_score)
    print ("The sum of scores: ", sum)
    print ("The average score is: ", average)
    print ("The median score is: ", median)
    print ("The lowest score is: ", lowest)
    print ("The higest score is: ", highest)
    print ("The standard dev is: ", stDev)
  
main()
