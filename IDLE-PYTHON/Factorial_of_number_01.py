# Find the factorial of given number!

def fact(a):
    if a == 0: 
       return 1
    else: 
        return ((a)*fact(a - 1))
    
num = int(input("Enter the number : "))

result = fact(num)
print("Factorial of the given number :", result)
