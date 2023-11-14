# Genrating the prime numbers in intervals 

limit_start = int(input("Enter the starting number  : "))
limit_ending = int(input("Enter the ending number  : "))

for x in range(limit_start, limit_ending +1 ):
    if x > 1 : 
        for i in range(2, x): 
            if x%i == 0:
                 break 
        else: 
            print(x)
