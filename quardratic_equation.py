import math 

# Taking input from user!
a = int(input("Enter The cofficent of x2 : "))
b = int(input("Enter The Cofficent of x : "))
c = int(input("Enter The Constant : "))

d = b**2 - 4*a*c

if d > 0 : 
    x = (-b + math.sqrt(d/2*a))
    y = (-b - math.sqrt(d/2*a))
    print("Roots are real and unequal : " , x, "and : " , y  )
elif d == 0: 
    x = -b/2*a 
    print("Roots are real and equal : " ,x )
else : 
    print("No roots are here")

#Take output through by run the program ; 

