def factorial(num):
    x=1
    if num>0:
        for i in range(1,num+1):
           x=x*i

    print("Factorial of ",num,"is",x)