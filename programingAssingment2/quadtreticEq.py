# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath
def quadtraticEq():
    a = int(input("Enter the first value of Quadtretic Equation : "))
    b = int(input("Enter the second value of Quadtretic Equation : "))
    c = int(input("Enter the third value of Quadtretic Equation : "))
    # calculate the discriminant
    d=(b**2)-(4*a*c)
    # find two solutions
    sol1=(-b+(d**0.5))/(2*a)
    sol2=(-b-(d**0.5))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))