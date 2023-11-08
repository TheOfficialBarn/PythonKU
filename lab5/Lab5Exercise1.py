'''
Author: Aiden Barnard
KUID: 3108416
Start date: Friday, October 6, 2023
Due: Friday, October 13, 2023
Lab: lab5Exercise1
Last modified: Thursday, October 12, 2023
Purpose: This lab builds off of 2D lists along and for in loops; the goal is to create a python file that interprets data from Input.txt and create new files that lists information of the input.
'''

InputFile=input('What is the name of the file you would like to obtain floats from?: ')
InputFile=open(InputFile, 'r')

#New files:
avgsFile=open('averages.txt','w')
rvrsFile=open('reverse.txt','w')
flipFile=open('flip.txt','w')
origFile=open('Orig.txt', 'w')
#The creation of dgnlFile depends on an if statement later on

grid=[]
for line in InputFile:
    rowList=line.strip().split(' ')
    grid.append(rowList)
#Each line is a "rowList"

dgnl=False
if grid[0][0] == grid[0][1]:
    dgnlFile=open('diagnol.txt','w')
    dgnl=True

#This line of code is for the final transpose. It makes it easier for me to do it with these numbers rather than using lengths.
rowAmnt= int(grid[0][0])
colAmnt= int(grid[0][1])

#The following removes the initial list in grid as it doesn't contain values applicable to the satistics
del grid[0]


#This for in loop turns the 2D list into floats which were originally strings.
for rowIndex in range(len(grid)):
    for colIndex in range(len(grid[rowIndex])):
        grid[rowIndex][colIndex]= float(grid[rowIndex][colIndex])



#AVERAGES FILE
averageList=[]
for rowIndex in range(len(grid)):
    average=sum(grid[rowIndex])/len(grid[rowIndex])
    averageList.append(average)

totalAverage=str(sum(averageList)/len(grid))

avgsFile.write('Total average: '+totalAverage)
for index in range(len(grid)):
    averageList[index]=str(averageList[index])
    index=str(index)
    avgsFile.write('\nRow '+index+' average: '+averageList[int(index)])

#REVERSE FILE
myDelimiter=' '
for row in grid:
    row.reverse()

for rowIndex in range(len(grid)):
    for colIndex in range(len(grid[rowIndex])):
        grid[rowIndex][colIndex]= str(grid[rowIndex][colIndex])
    reversedString= myDelimiter.join(grid[rowIndex])
    rvrsFile.write(reversedString+'\n')

#FLIPPED FILE
grid.reverse()
for row in grid:
    row.reverse() #Gotta make sure the numbers in the rows back in order first

for rowIndex in range(len(grid)):
    flippedString= myDelimiter.join(grid[rowIndex])        
    flipFile.write(flippedString+'\n')

#DIAGNOL FILE
grid.reverse()
if dgnl is True:
    for rowIndex in range(len(grid)):
        for colIndex in range(len(grid[rowIndex])):
            dgnlFile.write(grid[colIndex][rowIndex]+' ')
        dgnlFile.write('\n')

#ORIGINAL FILE TRANSPOSE
for colIndex in range(colAmnt):
    for rowIndex in range(rowAmnt):
        origFile.write(grid[rowIndex][colIndex]+' ')
    origFile.write('\n')