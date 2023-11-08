'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 22, 2023
Due: Friday September 29, 2023
Lab: lab03-exercise0169
Last modified: Friday, September 29, 2023
Purpose: a user fills out two lists of integer, and a program will print statistics based on the lists. All values that appear in both lists should appear too; duplicate contents will be removed.
'''

intList1= []

while True:
    list1Prompt= int(input('Enter a value for the first list: '))
    intList1.append(list1Prompt)

    donePrompt= input('Are you done? (y|Y): ')
    if donePrompt.lower() == 'y':
        break
    elif donePrompt.lower() != 'n':
        print('Try again!')

intList2= []

while True:
    list2Prompt= int(input('\nEnter a value for the second list: '))
    intList2.append(list2Prompt)

    donePrompt= input('Are you done? (y|Y): ')
    if donePrompt.lower() == 'y':
        break
    elif donePrompt.lower() != 'n':
        print('Try again!')
#As long as the user continues to enter y for the while loops, they will be continuously prompted to enter integers that go into either list 1 or list 2.

sum1=0
average1=0
sum2=0
average2=0
commonValues=0
overlappingValues=[]
uniqueValues=[]
#Declaring my variables

for num in intList1:
    sum1+= num
    if num in intList2:
        commonValues+= 1
        overlappingValues.append(num)
        #This adds overlapping values to overlappingValues list
    if num not in uniqueValues:
        uniqueValues.append(num)
        #This adds unique values to the list uniqueValues
for num in intList2:
    sum2+= num

average1= sum1/len(intList1)
average2= sum2/len(intList2)

print('\nList statistics: ')

if sum1 > sum2:
    print('The first list has the larger sum of', sum1)
elif sum1 ==sum2:
    print('The lists have the same sum of', sum1)
else:
    print('The second list has the larger sum of', sum2)
#Sum COmparison
if average1 > average2:
    print('The first list has the larger average of', average1)
elif average1 ==average2:
    print('The lists have the same average of', average1)
else:
    print('The second list has the larger average of', average2)
#Average Comparison
print('Count of values that appear in both lists: ', commonValues, '\nThese values are', overlappingValues)
print('Here are the non-duplicate values: ', uniqueValues)
#Unique and Common Values Test
if intList1 == intList2[::-1]:
    print('The lists are mirrors of each other.')
else:
    print('The lists are not mirrors of each other.')
    #Mirror Test