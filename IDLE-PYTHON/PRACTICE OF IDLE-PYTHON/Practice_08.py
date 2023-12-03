# Creating the quadratic equation solving python program 

# importing the math moduel
import math 

# Taking the user from input 
a = int(input("Enter the cofficent of x^2 : "))
b = int(input("Enter the cofficent of x   : "))
c = int(input("Enter the constant         : "))

# Appling the Formula 

d = b**2 - 4*a*c 

# Using the if and else 

if d > 0 :
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print(f"The {x1} and {x2} are Real and Unequal roots")

elif d == 0: 
    x3 = -b/(2*a)
    print(f"The {x3} is a real and equal roots")
else:
    print("No roots are here! ")
