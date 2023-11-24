n = int(input("Enter the number : "))

for i in range(1 , 11): 
    print(n ,"x", i , "=", n*i )

# check the given number is prime or not

num = int(input("Enter the number : "))

if num == 1: 
    print(f"{num} is not a prime number" )
if num > 1:
    for i in range(2, num):
        if num%i==0:
            print(f"{num} is not a prime number!")
            break
    else: 
        print(f"{num} is a prime number!")

