import math


def fibonacciNum(n):
    if n < 0:
        print("invalid value")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return (fibonacciNum(n-1)+fibonacciNum(n-2))

def factorial(n):

    if n==1:
        return 1;
    else:
        return (n * factorial(n-1))

def bodyMass(w,h):
    return(w/h)

def calcLog(x):
    return math.log(x)

def sumCube(n):
    val=((n*(n+1))/2)**2
    return val

def programmingAssingment6():
    n=int(input("Enter the integer value to find out factorial"))
    print("Factorial of ",n," is ",factorial(n))

    length=int(input("Enter a value to find fibonacci num :"))
    print("Fibonacci number for ",length," is ",fibonacciNum(length))

    w=float(input("Enter your weight : "))
    h=float(input("Enter your height : "))
    print("Your Body Mass Index is : ",bodyMass(w,h))

    x=int(input("Enter value to find its natural log: "))
    print("Natural log value of ",x," is ",calcLog(x))

    n=int(input("Enter value to get cube of sum of natural num :"))
    print("Cube of sum of till n numbers :",sumCube(n))

