'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 15, 2023
Due: Friday September 22, 2023
Lab: lab02-exercise01
Last modified: Friday, September 22, 2023
Purpose: this exercise asks the user to enter a phrase with a sequence phrase to search for within the phrase. The user can conduct a case-sensitive/non case-sensitive search.  
'''


userString= input('Enter a string: ')
sequence= input('Enter a sequence to count: ')
caseSensitive= ''
#I set the variable here so that I can use it in a while loop without having to use the term break after if and else. Otherwise the while loop won't work.
while caseSensitive != 'y' and caseSensitive != 'Y' and caseSensitive != 'n' and caseSensitive != 'N':
        caseSensitive= input('Do you want case-sensitive match? (y/n): ')

        if caseSensitive == 'y' or caseSensitive == 'Y':
                sequenceCount= userString.count(sequence)
                print(sequence, 'appears', sequenceCount, 'times.')
                
        elif caseSensitive == 'n' or caseSensitive == 'N':
                userString= userString.lower()
                sequence= sequence.lower()
                sequenceCount= userString.count(sequence)
                print(sequence, 'appears', sequenceCount, 'times.')
        else:
                print('Please type y/n for the case-sensitive prompt.')
                #Here, I want Python to ask the user to enter y/n for caseSensitive
        