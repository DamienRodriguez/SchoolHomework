#Damien Rodriguez
#Assignment: 6
#Purpose: To create a dynamic list, display median and mean, all menu driven


def main():
    
    dynamicList = []            #To me dynamic means that it will always change
    choice = displayMenu()      #Priming the while loop
    done = False                #Priming another while loop

    while choice != '6':

        if choice == '1':

            while True:                                 #might put into its own seperate function but don't see the reason to
                try:
                
                    userAdd = int(input("Enter the number you would like to submit: "))
                    
                    if userAdd < 0:                                                     
                        print("Invalid Response. Please Enter a positive integer.")
                    else:
                        dynamicList.append(userAdd)
                        break
                except:
                    print("Please enter valid data.")

        
        if choice == '2':
            displayMean(dynamicList)
            
        if choice == '3':
            displayMedian(dynamicList)
            
        if choice == '4':
            print(dynamicList)
            
        if choice == '5':
            print("Coming soon.")

        choice = displayMenu()
        

    print("Thank you for grading my program!")

#=============================================================================
# Purpose: To display the median of a given list
# Input: dynamicList - list that is created by the user at the start
# Output: no output

def displayMedian(dynamicList):

    length = 0
    median = 0

    length = len(dynamicList) // 2

    if len(dynamicList) % 2 == 1:
        print(dynamicList[length + 1])
    else:
        median = dynamicList[length] + dynamicList[length + 1]
        median = median / 2
        print(median)
#=============================================================================

#=============================================================================
# Purpose: To display the mean of a given list
# Input: dynamicList - list that is created by the user at the start
# Output: no output

def displayMean(dynamicList):

    total = 0
    lengthOfList = len(dynamicList)
    for x in range(lengthOfList):
        total += dynamicList[x]

    print(total / lengthOfList)
    
#=============================================================================



#=============================================================================
# Purpose: To display the given menu
# Input: There is no input
# Output: choice = character value that will determine what path
#                  to take in the menu
def displayMenu():

    choice = '0'
    
    while choice != '1' and choice != '2' and choice != '3' and \
          choice != '4' and choice != '5' and choice != '6':

        
        print (""" \n\nPlease choose one of the following
            1. Add a number to the list
            2. Display the mean
            3. Display the median
            4. Print the list to the screen
            5. Print the list in reverse order
            6. Quit""")

        
        choice = input("Please enter an option --> ")

        if choice != '1' and choice != '2' and choice != '3' and \
        choice != '4' and choice != '5' and choice != '6':
            print("Invalid Option. Please select again.")
        



    return choice
#=============================================================================

main()
    
