num = int(input("Enter the chekcing the value : "))

if num == 1: 
    print("this is not a prime number")
elif num > 1: 
    for i in range(2 , num): 
        if num%i == 0: 
            print("This is not a prime number")
            break 
    else: 
        print("This is a prime number")
