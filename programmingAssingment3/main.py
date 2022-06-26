# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import leapYear
import oddEven
import positiveNegativeZero
import primeNumber


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    x=int(input("Enter the value to check : "))
    positiveNegativeZero.positiveNegZero(x)

    x=int(input("Enter the value to check even or odd : "))
    oddEven.oddEven(x)

    year=int(input("Please enter year to check if leap year or not :"))
    leapYear.leapYear(year)

    num=int(input("Please enter the value to check prime number :"))
    primeNumber.primeNum(num)

    lower=int(input("Enter the lower value to check prime num : "))
    higher=int(input("Enter the higher value to check prime num : "))
    primeNumber.primeNumList(lower,higher)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
