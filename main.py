# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hcfCalc
import lcmCalc
import numSysConv
import simpleCalc


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    x=int(input("Enter the first value to find LCM : "))
    y=int(input("Enter the second value to find LCM : "))
    print("LCM of ",x,"and",y," is: ",lcmCalc.computeLCM(x,y))

    x=int(input("Enter the first value to find HCF : "))
    y=int(input("Enter the second value to find HCF : "))
    print("HCF of ",x,"and",y," is: ",hcfCalc.computeHCF(x,y))

    numSys=input("Enter the name of number system you want to change to : ")
    decNum=int(input("Enter the decimal number to convert : "))
    result=numSysConv.numSysCon(numSys,decNum)
    print("Value of ", decNum, " in the ",numSys," is ",result)

    char=input("Enter a character to find out its ASCII value : ")
    print("The ASCII value of ",char," is ",ord(char))

    simpleCalc.simpleCal()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
