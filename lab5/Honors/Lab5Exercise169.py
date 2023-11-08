'''
Author: Aiden Barnard
KUID: 3108416
Start date: Friday, October 6, 2023
Due: Friday, October 13, 2023
Lab: lab5Exercise169
Last modified: Sunday, October 12, 2023
Purpose: This final exercise is a Wheel-of-Fortune-esque game that prompts a user to enter five letters and guess a secret phrase.
'''

phrase='Closed on Sunday'.upper()

#Begginning of game.
print("Let's play WHEEL OF PYTHON!")
letterGuess= input('Choose 5 letters to help: ').upper()

#The following ensures the user picks only five letters.
while len(letterGuess) != 5:
    print('Pick ONLY FIVE letters. Try again.')
    letterGuess= input('Choose 5 letters to help: ').upper()

finalList=[]
for letter in phrase:
    if letter in letterGuess:
        finalList.append(letter)
    elif letter is ' ':
        finalList.append(letter)
    else:
        finalList.append('?')

print('Here is your phrase: \n', ''.join(finalList))

finalGuess=input('Enter your guess: ').upper()

if finalGuess == phrase:
    print('You win!')
else:
    print('You lose!')