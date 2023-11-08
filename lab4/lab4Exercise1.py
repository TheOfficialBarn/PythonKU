'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 29, 2023
Due: Friday, October 6, 2023
Lab: lab4Exercise1
Last modified: Thursday, October 6, 2023
Purpose: This program is a for-in loop that tracks the history of a "Web Browser"; however, there are exceptions; one cannot revist a site or visit a non-secured page!
'''


#Below includes the .txt input and output files
userPrompt=input('Enter input file name: ')
textInput=open(userPrompt,'r')
textOutput=open('OutputFile.txt','w')

#Below is the file's history
commandHistory=[]
navHistory=[]


#List of COMMANDS to be used:
nav='NAVIGATE'
back='BACK'
ford='FORWARD'
hist='HISTORY'
end='EXIT'


#Here is the pointer system. The pointer should indicate the current site you are on.
pointer= '<=='
pointerLocation=0

for line in textInput:
    line=line.strip()
    commandHistory= line.split(' ')
    
    #These if/elif blocks are in the for in loop
    if commandHistory[0] == nav and commandHistory[1].startswith('https://') and commandHistory[1] not in navHistory:
        navHistory.append(commandHistory[1])

        #This should remove any links located after the pointer when a user proceeds to navigate again.
        if pointerLocation != -1:
            del navHistory[pointerLocation+1:-1]

        pointerLocation= len(navHistory)-1

    elif commandHistory[0] == nav and not commandHistory[1].startswith('https://'):
        print('Enter a secure link into the InputFile and try again!')
        break
    elif commandHistory[0] == nav and commandHistory[1] in navHistory:
        print('You cannot revist a recently visisted link that is in history still.')
        break
    elif commandHistory[0] == back:
        pointerLocation-=1

    elif commandHistory[0] == ford:
        pointerLocation+=1

    elif commandHistory[0] == hist:
        #Beginning of each history request
        textOutput.write('Oldest\n===========\n')
        navHistory[pointerLocation]=navHistory[pointerLocation]+' <=='
        
        for url in navHistory:
            url=url.strip()
            textOutput.write(url+'\n')
        
        textOutput.write('===========\nNewest\n\n')

        navHistory[pointerLocation] = navHistory[pointerLocation].replace('<==',' ')
        #End of each history request
    elif commandHistory[0] != end:
        textOutput.write('Ensure all COMMANDS are uppercase and valid. Try again.')

#This statement resides outside the for–in loop due to the fact that it only ever is called once and always at the end.
if commandHistory[0] == end:
    textInput.close()
    textOutput.close()
    print("Program ended. All files have closed succesfully!")

#Again, you have to close the file outside the loop, otherwise there will be a loop error.
elif commandHistory[0] == nav and not commandHistory[1].startswith('https://'):
    textInput.close()
    textOutput.close()
    print("Program ended. All files have closed succesfully!")

#This is the third possible scenario of leaving the loop (link revist)
elif commandHistory[0] == nav and commandHistory[1] in navHistory:
    textInput.close()
    textOutput.close()
    print("Program ended. All files have closed succesfully!")

