'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 22, 2023
Due: Friday September 22, 2023
Lab: lab02-exercise169
Last modified: Friday, September 22, 2023
Purpose: this exercise is an extension of exercise 2. Each letter has to be in the correct spot, and you have to call the amount of guesses you get in advance.
'''


secretPhrase= 'bringcoffee'
guess= ''
guessLimit= int(input("How many guesses do you think you can get the phrase in? You will be limited to this number!\n Guess Limit: "))
attemptNumber=0

while attemptNumber < guessLimit:
    correctLetters=0
    correctLetterPositions= []
    attemptNumber += 1
    print("You are on attempt: ", attemptNumber)
    guess= input('Guess the secret phrase!\nGuess: ').lower()

    if attemptNumber== guessLimit and guess != secretPhrase:
        print("\n\nTake the L")
        #DEFEAT


    elif guess == secretPhrase:
        print('\nCongratulations! You guessed the secret phrase.')
        #VICTORY


    elif len(guess) == len(secretPhrase):
        print("\nYou have the correct amount of letters! You're close!")

        for letter in range(len(secretPhrase)):
            if guess[letter] == secretPhrase[letter]:
                correctLetterPositions.append(secretPhrase[letter])
                correctLetters+= 1
        
        print("Correct Letters: ",correctLetters)
        print("Correctly Positioned Letters: ", ', '.join(correctLetterPositions))
        #CORRECT LETTER AND CORRECT POSITION


    elif len(guess) > len(secretPhrase):
        print('\nYou have gussed too many letters. Try again!\n')
        #TOO LONG


    else:
        print('\nConsider trying a longer guess. Try again!\n')
        #TOO SHORT