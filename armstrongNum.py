def armstrong(num):
    tmp=num
    sum=0
    order=len(str(num))
    while tmp >0 :
        digit=tmp%10
        sum+=digit**order
        tmp//=10
    if sum==num:
        print("num is a armstrong")
    else:
        print("num is not a armstrong")

#armstrong(1634)