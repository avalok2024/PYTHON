def is_prime(num): 
    if num <= 1:
        return False 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True

def genrate_prime_num(n):
    primes_numbers = [ ]
    num  = 2 
    while len(primes_numbers)< n: 
        num += 1 
    return primes_numbers
n = int(input("Enter the Value of n : "))
prime_numbers = genrate_prime_num(n)
print(f"The first {n} prime numbers are: { prime_numbers}" )