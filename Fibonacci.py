def Finbonacci(n):
    a=0
    b=1
    l=[]
    if n < 0:
        print("Invalid value")
    elif n==0:
        return 0
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
            l.append(b)
        return l

#print(Finbonacci(9))

