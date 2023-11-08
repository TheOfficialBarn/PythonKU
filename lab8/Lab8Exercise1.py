'''
Author: Aiden Barnard
KUID: 3108416
Start date: Friday, November 3, 2023
Due: Friday, November 10, 2023
Lab: Lab8Exercise1
Last modified: 
Purpose:
'''

import random

def menu():
    print('1)\tPrint Pokedex\n2)\tTranslate\n3)\tBuild a team\n4)\tPokemon battle\n5)\tFight Log\n6)\tExit\n')

def menuChoice(option, pokeDict):

    if option == 1: #Print Pokedex
        print(pokeDict)
    elif option == 2: #Translate
        USname=input('What US pokemon do you want the JPN name of?: ')
        print(pokeDict[USname])
    elif option == 3: #Build a team
        teamList=[]
        size=int(input('If you would like to specify a team size, enter one here. Otherwise only click enter: '))
        while True:
            isUnique=input('Would you like your team members to be unique? (y/n): ')
            if isUnique == 'y':
                isUnique=True
                break
            elif isUnique =='n':
                isUnique=False
                break
            else: 
                print('Choose a valid response!')
        
        buildTeam(pokeDict, size, isUnique)
    elif option == 4: #Pokemon battle
        team1=teamList[#randomnumber]
        team2=teamList[#randomnumber]
        print(battle(team1,team2))
    elif option == 5: #Fight log
        print("Create a fight log")
    elif option == 6: #Exit
        print("Create something to close the file")
    else:
        print('Pick a valid option between 1 and 6!')
    return

def buildPokedex(filename):
    pokedexFile=open(filename,'r')
    pokeDict={}
    for line in pokedexFile:
        lineList=line.split()
        pokeDict[lineList[0]]=lineList[1]
    return pokeDict

def buildTeam(pokeDict, size=6, isUnique=False):
    return
def battle(team1,team2):
    return 

def fightLog(#Parameters):
    return

def main():
    pokeDict=buildPokedex(input('Enter the name of your Pokedex file: '))
    menu()
    menuChoice(int(input('Select a choice from above: ')),pokeDict)

    

main()