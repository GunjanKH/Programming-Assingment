def primeNum(num):
    flag=False
    if  num >1 :
        for i in range(2,num):
            if num%i==0:
                flag=True
                break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

def primeNumList(x,y):
    for num in range(x,y+1):
        if num>1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                print(num,"is a prime number")