# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import calendar

import calenderNew
import celciusToFarenheit
import kmToMiles
import quadtreticEq
import swapVar


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Km to miles convertion
    km=float(input("Please enter the KM value to be converted :"))
    kmToMiles.kmToMiles(km)
    #cel to farenheit convertion
    cel=float(input("Please enter the celcius value to be converted : "))
    celciusToFarenheit.celciusToFaremheit(cel)

    #Calender
    mm=int(input("Enter the month for calender : "))
    yy=int(input("Enter the year for calender : "))
    calenderNew.calenderNew(yy,mm)

    #Quadtratic Equation
    quadtreticEq.quadtraticEq()

    #Swap variable without using temp variable
    x=int(input("Enter First value to be swapped : "))
    y=int(input("Enter Scecond value to be swapped : "))
    swapVar.swapVari(x,y)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
