import math 
def equation(a, b, c):
    delta = b**2 - 4*a*c
    if a == 0:
        return f'This is linear equation and have roots is: {-c/b}'
    elif delta < 0:
        return 'Equation is no solution'
    elif delta == 0:
        return f'Equation with a double roots is {-b/2*a}'
    else:
        x1 = (-b + math.sqrt(delta))/(2*a) 
        x2 = (-b - math.sqrt(delta))/(2*a) 
        return f'Equation with two distinct roots is: {x1} và {x2}'

a = float(input("Please enter a number a: "))
b = float(input("Please enter a number b: "))
c = float(input("Please enter a number c: "))
print(equation(a,b,c))