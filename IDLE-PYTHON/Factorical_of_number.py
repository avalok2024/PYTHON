# # finding the factioral of numbers 

# num = int(input("Enter the number : "))
# fact = 1 
# if num < 0 :
#     print("Negative does not contain factorial")
# if num == 0 :
#     print("factorial of 0 is 1 ")
# if num > 0 : 
#     for i in range(1 , num+1):
#         fact = fact*i
# print("the factorial of the given number is", fact)

# or 

def fact(a): 
    if a == 0:
        return 1 
    else: 
        return ((a)*fact(a - 1))
    
num = int(input("Enter your number : "))

result = fact(num)
print("The factorial of given number is : ",result)
