# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Fibonacci
import armstrongNum
import armstrongNumList
import factorial
import multipication
import sumNaturalNum


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # print_hi('PyCharm')
   num=int(input("Enter the value to find out its factorial : "))
   factorial.factorial(num)

   n=int(input("Enter the value to find out multiplication table : "))
   multipication.multipication(n)

   x=int(input("Enter the value to find out Fibonacci Series : "))
   print(Fibonacci.Finbonacci(x))

   y=int(input("Enter the value to check Armstrong Number : "))
   armstrongNum.armstrong(y)

   num1=int(input("Enter the first value of the list to find out Armstrong Num: "))
   num2=int(input("Enter the last value of the list to find out Armstrong Num: "))
   armstrongNumList.armstrongNumList(num1,num2)

   num3=int(input("Enter a natural number to get the sum of it :"))
   sumNaturalNum.sumNatual(num3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
