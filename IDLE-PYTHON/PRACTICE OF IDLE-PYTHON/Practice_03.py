# gerating the prime numbers with in the limits 

start = int(input("Enter the starting limit  : "))
last = int(input("Enter the last limit : "))

for x in range(start , last+1 ):
    if x > 1 :
        for i in range(2, x): 
            if x%i == 0: 
                break
        else:
            print(x)

            