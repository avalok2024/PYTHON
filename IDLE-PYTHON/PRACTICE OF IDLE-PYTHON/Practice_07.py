def primes(num): 
    if num <= 1: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: 
            return False
        return True
    
def genreate_primes_number(n): 
    prime_number = [ ]
    num = 2 
    while len(prime_number) < n : 
        if primes(num):
            prime_number.append(num)
        num += 1 
    return prime_number
 
n = int(input("Enter the value of n : "))

prime_number = genreate_primes_number(n)
print(f"the first {n} prime number are {prime_number}")
