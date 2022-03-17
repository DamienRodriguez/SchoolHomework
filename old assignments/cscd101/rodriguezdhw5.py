#Damien Rodriguez
#Assignment: 5
#Purpose: To create a RNG and linear search that is menu driven

from random import randint

def main():
    userList = createList()

    choice = displayMenu()          #Priming while loop with user choice
    

    while choice != '4':            #Allows for menu to be called lots of times

        if choice == '1':
            userList = createList()
        elif choice == '2':
            print(userList)         #No sense in creating a function to print something when it is already there
        elif choice == '3':
            linearSearch(userList)

        choice = displayMenu()

    print("Thank you for your time.")




#=======================================================
# Purpose: To make a linear search of the list for a number given by the user
# Input: userList - int list of 5 random numbers generated
# Output: no output

def linearSearch(userList):
    
    try:                                                            #Working with this to see how it works
        number = int(input("What number are you looking for? "))
        found = False
        position = 0

        while position < len(userList) and not found:                   #Takes set position of 0 and goes till it finds (or not) your number
            if userList[position] == number:   
                found = True
            position += 1


        if found == True:
            print("This works")
            print("Found it! " + str(number) + " is in the index of " + str(position - 1))
        else:
            print(-1)


    except:
        print("Invalid input")
#=======================================================
    
#=======================================================
# Purpose: To create a 5 element list containing random integers
# Input: There is no input
# Output: userList - list created within this function

def createList():
    userList = []

    for x in range(5):
        userList.append(randint(1,9))                                   #Creates 5 random numbers from range 1 to 9

    return userList



#=============================================================================
# Purpose: To display the given menu
# Input: There is no input
# Output: choice = character value that will determine what path
#                  to take in the menu
def displayMenu():

    choice = '0'

    while choice != '1' and choice != '2' and choice != '3' and \
          choice != '4':
        print (""" \n\nPlease choose one of the following
            1. Create a new list of 5 random integers
            2. Displays current list
            3. Search list for a particular number
            4. Quit """)
        choice = input("Please enter an option --> ")

        if choice != '1' and choice != '2' and choice != '3' and  \
           choice != '4':
            print("Invalid Option. Please select again.")



    return choice
#=============================================================================

main()
