# Damien Rodriguez
# Assignment: 1
# Purpose: To determine age of individual upon graduation
# Submitted on: 9/26/2017 @ 3:10 PM
# Extra Credit attempted


def main():
    ageInYears = 0
    ageInMonths = 0

    birthYear = int(input("Please enter your birth year: "))
    birthMonth = int(input("Please enter your birth month: "))
    birthDay = int(input("Please enter your birth day: "))
    
    

    gradYear = int(input("Please enter your graduation year: "))
    gradMonth = int(input("Please enter your graduation month: "))
    gradDay = int(input("Please enter your graduation day: "))
    
    


    if gradMonth < birthMonth:
        ageInYears = gradYear - birthYear - 1
        ageInMonths = 12 - gradMonth + 12 - birthMonth #this works here
    elif gradMonth == birthMonth and birthDay > gradDay:
        ageInYears = gradYear - birthYear - 1
        ageInMonths = 12 - 1
    else:
        ageInYears = gradYear - birthYear
        ageInMonths = gradMonth - birthMonth #math works here


    
    print("Your age will be " + str(ageInYears) + " years and " + str(ageInMonths) + " months old when you graduate.")
main()
        
