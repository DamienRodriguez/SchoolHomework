#Name: Damien Rodriguez
#Assignment: 3
#Purpose: To design a menu driven program that takes numbers
#and does things with them

import math


def main():

    number = getNumber()
    
    choice = displayMenu()
    while choice != '5':
        
        if choice == '1':
            number = getNumber()
        elif choice == '2':
            kindsOfNumbers(number)
        elif choice == '3':
            primes(number)
        elif choice == '4':
            sumOfDigits(number)
        
        choice = displayMenu()

    print("\nThank you! \n\n")




#=============================================================================
# Purpose: To get a number from the user
# Input: There is no input
# Output: number - the number that the user gave

def getNumber():

    number = -1

    true = True

    while number < 0:
        number = int(input("Please enter a non-negative number: "))

        if number < 0:
            print("Invalid number. Please try again.")

        true = False

    return number

#=============================================================================


#=============================================================================
# Purpose: To display the given menu
# Input: There is no input
# Output: choice = character value that will determine what path
#                  to take in the menu
def displayMenu():

    choice = '0'
    while choice != '1' and choice != '2' and choice != '3' and \
          choice != '4' and choice != '5':
        print (""" \n\nPlease choose one of the following
            1. Enter a number
            2. Print number of odd, even, and zero digits in your given number
            3. Print prime numbers between 2 and the number you provided
            4. Print the sum of the digits of your provided number
            5. Quit""")
        choice = input("Please enter an option --> ")
        if choice != '1' and choice != '2' and choice != '3' and  \
           choice != '4' and choice != '5':
            print("Invalid Option. Please select again.")



    return choice
#=============================================================================

#=====================================================================
# Purpose: To determine the what kinds of numbers make up the users
#          inputted number
# Input: number - users inputted number
# Output: Nothing will be returned. Just displayed

def kindsOfNumbers(number):

    evens = 0
    odds = 0
    zeroes = 0
    

    true = True
    while true == True:
        digit = number % 10

        if digit == 0:
            zeroes += 1
        elif digit % 2 == 0:
            evens += 1
        elif digit % 2 == 1:
            odds += 1

        number = number // 10

        if number == 0:
            true = False

    print(str(evens) + " even numbers.\n")
    print(str(odds) + " odd numbers.\n")
    print(str(zeroes) + " zero numbers.\n")
            
    return 0
#=============================================================================

#================================================================================
# Purpose: To determine the primes between 2 and the users input
# Input: number - users inputted number
# Output: Nothing will be returned. Just Displayed

def primes(number):
    myList = []

    for x in range(1,number):
        if(math.factorial(x) % (x + 1) == x):
            myList.append(x + 1)
    print("The list presented is the prime numbers between 2 and " + str(number) + "\n " + str(myList))

#=================================================================================

#==============================================================================
# Purpose: To count the sum of the numbers from the users input
# Input: number - users inputted number
# Output: Nothing will be returned. Just displayed

def sumOfDigits(number):

    sumOfNumbers = 0

    true = False

    while true == False:

        digit = number % 10
        sumOfNumbers += digit

        number = number // 10

        if number == 0:
            true = True
    
    print("Here is the sum of the digits in your number: " + str(sumOfNumbers))

#================================================================================

main()


            
