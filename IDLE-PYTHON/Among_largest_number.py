# Find the largest number in three numbers!

a = int(input("Enter the number of a : "))
b = int(input("Enter the number of b : "))
c = int(input("Enter the number of c : "))

# if a > b and a > c : 
#     print("a is the largest number") 
# elif b > a and b > c: 
#     print("b is the largest number")
# else: 
#     print("c is the largest number")

# OR

if a > b or b > c :
    if a > b :
        print("a is the greatest number")
    else: 
        print("b is the greatest number")
else: 
    print("c is the greatest number")