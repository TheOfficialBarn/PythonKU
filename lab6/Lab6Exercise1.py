'''
Author: Aiden Barnard
KUID: 3108416
Start date: Friday, October 13, 2023
Due: Friday, October 27, 2023
Lab: lab6Exercise1
Last modified: Thursday, October 26, 2023
Purpose: This lab utilizes functions to do several different tasks with integers.
'''

#Unpickable functions for use in other functions
def lastDigit(num):
    num%=10
    return num
def removeLastDigit(num):
    num//=10
    return num
def addDigit(num, newDigit):
    num*=10
    num+=newDigit
    return num
def printMenu():
    print("\n1) Count digits\n2) Sum digits\n3) Is Palindrome\n4) Reverse\n5) Prime Detector\n6) Exit")
    return
#------------------------------------------------------------------------------------------------------
def countDigits(num):
    digitAmount=0
    while num != 0:
        num=removeLastDigit(num)
        digitAmount+=1
    return digitAmount
def sumDigits(num):
    sum=0
    while num !=0:
        sum+=lastDigit(num)
        num=removeLastDigit(num)
    return sum
def isPalindrome(num):
    if reverse(num) == num:
        num=True
    else:
        num=False
    return num
def reverse(num):
    newNum=0
    while num != 0:
        newNum=addDigit(newNum, lastDigit(num))
        num=removeLastDigit(num)
    return newNum
def primeDetector(num):
    prime=True
    if countDigits(num) >=8:
        print('\nLoading...\nIntegers with digit amounts greater than 8 may take a few moments to process.')
    for numTests in range(2,num):
        if num%numTests == 0:
            prime=False
    return prime
#------------------------------------------------------------------------------------------------------
def main():
    while True:
        numPick=-1
        while numPick<0:
            numPick=int(input("Enter any positive integer: "))
            if numPick <0:
                print("Please enter a valid positive integer.")
    
        printMenu()
        choice=int(input("Choice: "))

        if choice == 1: #Count digits
            print(countDigits(numPick))
        elif choice == 2: #Sum digits
            print(sumDigits(numPick))
        elif choice == 3: #Is Palindrome 
            if isPalindrome(numPick)==True:
                print('The number', numPick, 'is a palindrome.')
            else:
                print('The number', numPick, 'is not a palindrome.')
        elif choice == 4: #Reverse
            print(reverse(numPick))
        elif choice == 5: #Prime Detector
            if primeDetector(numPick) == True:
                print('The number', numPick, 'is a prime integer.')
            else:
                print('The number', numPick, 'is not a prime integer')
        elif choice == 6: #Exit
            print("Goodbye!")
            break
        else:
            print("Please select a valid choice.")

#Below actually executes the "main" function of the program.
main()