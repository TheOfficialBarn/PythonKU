'''
Author: Aiden Barnard
KUID: 3108416
Date: Friday, September 22, 2023
Due: Friday September 29, 2023
Lab: lab03-exercise01
Last modified: Friday, September 29, 2023
Purpose:  In this program, a user can add, check off, and print a shopping/grocery list that he/she makes.
'''

shoppingList=[]

while True:
    print('\nWelcome to your Shopping List!')
    print('1) Add item\n2) Check off item\n3) Print list\n4) Exit')
    choice= input('\nEnter a choice: ')
    
#This while statement gives the user a selection of inputs to choose from.

    if choice == '1':
        toAdd= input('What will you add to the list?: ')
        shoppingList.append(toAdd)
        #This adds the choice to the list.
    elif choice == '2':
        toCheck= int(input('Which item will you check off?: '))-1
        if 0 <= toCheck <len(shoppingList):
            item= shoppingList[toCheck]
            itemOff= item[0] + '-'*(len(item)-2) + item[-1]
            shoppingList[toCheck]=itemOff
        #this if statement checks to make sure that the entered integer is a valid option and proceeds to store the first and last letter to itemOff (item checked off list) along with dashes for the middle characters.
    elif choice == '3':
        print('Here is your list:')
        for num in range(len(shoppingList)):
            print(num+1, ')', shoppingList[num])
        #The for in loop prints the list in a vertical format.
    elif choice == '4':
        print('Goodbye!\n')
        break
    else:
        print('Choose a valid option please.\n')

    #With the if, elif, and else blocks, the program decides which task to do depending on the integer the user selected between 1 and 4.