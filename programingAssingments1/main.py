# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import areaOfTriangle
import arithmeticOperation
import helloPython
import swapNum
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    helloPython.hello()
    a=int(input("input first number :"))
    b=int(input("input second number: "))
    arithmeticOperation.arithmeticOperation(a,b)
    x=float(input("First side of Triangle:"))
    y=float(input("Second side of Triangle:"))
    z=float(input("Thired side of Triangle:"))
    areaOfTriangle.areaTriangle(x,y,z)
    num1=input("input first number: ")
    num2=input("input second number: ")
    swapNum.swapNum(num1,num2)

    print("Random number generated :",random.randint(0,100))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
