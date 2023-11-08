'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 22, 2023
Due: Friday September 22, 2023
Lab: lab02-exercise02
Last modified: Friday, September 22, 2023
Purpose: this exercise tries to get a user to guess a secret phrase. The while loop continues until the user gets the correct amount of letters and helps them find the solution.
'''


secretPhrase= 'bringcoffee'
guess= ''

while guess.lower() != secretPhrase:
    guess= input('Guess the secret phrase!\nGuess: ').lower()
    correctLetters=0

    if guess == secretPhrase:
        print('\nCongratulations! You guessed the secret phrase.')
        #GAME OVER
    elif len(guess) == len(secretPhrase):
        print("\nYou have the correct amount of letters! You're close!")
        for letters in range(len(secretPhrase)):
            if guess[letters] == secretPhrase[letters]:
                correctLetters += 1
        print("Correct Letters: ",correctLetters,"\n")

        #TRY AGAIN
    elif len(guess) > len(secretPhrase):
        print('\nYou have gussed too many letters. Try again!\n')
        #TRY AGAIN
    else:
        print('\nConsider trying a longer guess. Try again!\n')
        #TRY AGAIN