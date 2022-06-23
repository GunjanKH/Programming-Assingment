def areaTriangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("The area of triangle is: ",area)