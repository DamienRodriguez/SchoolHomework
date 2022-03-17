#Name: Damien Rodriguez
#Assignment: 4
#Purpose: Converting things, using a menu
#Extra credit attempted


def main():

    choice = displayMenu()
    while choice != '6':
        
        if choice == '1' or choice == '2':
            lengthConversion(choice)
        elif choice == '3':
            fahrenheitToCelsius()
        elif choice == '4':
            celsiusToFahrenheit()
        elif choice == '5':
            specialWord()
        
        choice = displayMenu()

    print("\nThank you! \n\n")


#=============================================================================
# Purpose: To display the given menu
# Input: No input
# Output: choice = character value that will determine what path
#                  to take in the menu
def displayMenu():

    choice = '0'
    while choice != '1' and choice != '2' and choice != '3' and \
          choice != '4' and choice != '5' and choice != '6':
        print (""" \n\nPlease choose one of the following
            1. Convert Feet to Meters
            2. Convert Meters to Feet
            3. Convert Fahrenheit to Celsius
            4. Convert Celsius to Fahrenheit
            5. See a special phrase backwards
            6. Quit """)
        choice = input("Please enter an option --> ")
        if choice != '1' and choice != '2' and choice != '3' and  \
           choice != '4' and choice != '5' and choice != '6':
            print("Invalid Option. Please select again.")



    return choice


#=============================================================================
# Purpose: To have a single function that allows for meter or foot conversion
# Input: choice - the users choice on which they want
# Output: No output

def lengthConversion(choice):
    
    feetConversion = 3.28084
    metersConversion = 0.3048

    feet = 0
    meters = 0
    unit = -1
    choice = int(choice)
    

    while unit < 0:
        if choice == 1:
            unit = float(input("please enter a non-negative number for feet: "))
        elif choice == 2:
            unit = float(input("please enter a non-negative number for meters: "))

        if unit < 0:
            print("Invalid number. Please try again.")

    if choice == 1:
        meters = unit * metersConversion
        print("\n\n" + str(unit) + " feet --> " + str(meters) + " meters.")
    
    elif choice == 2:
        feet = unit * feetConversion
        print("\n\n" + str(unit) + " feet --> " + str(feet) + " meters.")

#===============================================================================
# Purpose: To convert fahrenheit to celcius
# Input: No input
# Output: No ouput

def fahrenheitToCelsius():
    f = 0
    c = 0

    f = float(input("Please enter a value for Fahrenheit: "))

    c = (f - 32) * (5/9)

    print(str(f) + " Fahrenheit to Celcius is: " + str(c))


#===============================================================================
# Purpose: To display the given menu
# Input: No input
# Output: No output

def celsiusToFahrenheit():
    f = 0
    c = 0

    c = float(input("Please enter a value for Celcius: "))

    f = (c * (9/5)) + 32 

    print(str(c) + " Celcius to Fahrenheit is: " + str(f))

#===============================================================================
# Purpose: To display a word backwards
# Input: No input
# Output: No Output

def specialWord():

    print("Hello World" [::-1])


main()
    
        
    
        
        
