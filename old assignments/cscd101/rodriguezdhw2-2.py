# Damien Rodriguez
# Assignment: 2
# Purpose: To determine the amount an individual would have to pay in order to
# gain admission into a museum
# Extra credit for getting system date attempted
# Extra credit for screening for proper days in a month was attempted

import time, sys

def main():
    print("Hello, Welcome to Hopper's Computer Museum!")
    print("To determine your entrance fee, please enter the following: \n")

    dateBirth = input("Your Date of Birth (mm dd yyyy) --> ")
    coupon = input("Do you have a coupon (y/n)? --> ")
    dateToday = time.strftime("%m %d %Y")

    coupon = coupon.lower()

    birthArray = dateBirth.split(" ")
    todayArray = dateToday.split(" ")

    birthArray = list(map(int, birthArray))
    todayArray = list(map(int, todayArray))

    

    for month in (1,3,5,7,8,10,12):
        if(birthArray[0] == month and birthArray[1] > 31):
            print("You didn't input a valid day.")
            sys.exit()

    for month in (4,6,9,11):
        if (birthArray[0] == month and birthArray[1] > 30):
            print("You didn't input a valid day.")
            sys.exit()

    if (birthArray[0] == 2 and birthArray[1] > 28):
        print("You didn't input a valid day.")
        sys.exit()

    if coupon != 'y' and coupon != 'y':
        print("Invalid input")
        sys.exit()



    if (todayArray[0] < birthArray[0]):
        age = todayArray[2] - birthArray[2] - 1
    elif (todayArray[0] == birthArray[0] and birthArray[1] > todayArray[1]):
        age = todayArray[2] - birthArray[2] - 1
    else:
        age = todayArray[2] - birthArray[2]



    if(age <= 14):
        price = 5
    elif(age >= 15 and age <= 64):
        price = 9
    elif(age >= 65):
        price = 7.5



    if(coupon == 'y'):
        price -= 1

    price = '${:.2f}'.format(price)

    print("Your admission fee is: " + price + ", thank you for your visit!")

    return 0

main()
