'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 22, 2023
Due: Friday September 22, 2023
Lab: lab02-exercise03
Last modified: Friday, September 22, 2023
Purpose: this exercise asks a user how long the flu outbreak has occured for in order to compute the amount of total people sick.
'''


print("OUTBREAK")
peopleSick= [1,4,64]
#The values for the first three days.
outbreakDay= int(input("What day do you want a sick count for?: "))

if outbreakDay <= 0:
    print("Invalid day, enter another day: ")
    #Can't have a negative day.
elif outbreakDay > 0 and outbreakDay <= 3:
    print(peopleSick[outbreakDay-1], "are infected with the flu.")
    #Since the sum rule doesn't start until day 4, this prints out the values for the first 3 days given from the peopleSick variable.
else: 
    for i in range(3, outbreakDay):
            peopleSick.append(peopleSick[i-1]+peopleSick[i-2]+peopleSick[i-3])
            #This starts computing the sum of the last three days.
    print(peopleSick[outbreakDay-1], "are infected with the flu")