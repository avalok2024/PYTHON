# def primes(num):
#     if num <1: 
#         return False
#     for i in range(2, num + 1): 
#         if num%i == 0: 
#             print("This is a not a prime number!")
#         else : 
#             print("This is a prime number!")


num = int(input("Enter the number: "))

if num < 1:
    print("You can't take the negative number ")
elif num > 1: 
    for i in range(2, num +1): 
        if num % i == 0: 
            print("This is not a prime number!")
        else: 
            print("This is a prime number")
        break 
else: 
    print("zero is a not a prime number")
