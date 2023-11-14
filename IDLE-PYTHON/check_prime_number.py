# checking the given number is prime or not

num = int(input("Enter the number :"))

if num == 1 :
    print("This is not a prime number ")
if num > 1:
    for i in range( 2 , num ):
       if num%i == 0 :
           print("This is not a prime number")
           break
    else: 
        print("This is a prime number")
        