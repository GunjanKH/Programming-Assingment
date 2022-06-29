def armstrongNumList(x,y):
    for i in range(x,y):
        tmp=i
        sum=0
        order=len(str(i))
        while tmp > 0:
            digit = tmp % 10
            sum += digit ** order
            tmp //= 10
        if sum == i:
            print(i," is an armstrong number")


