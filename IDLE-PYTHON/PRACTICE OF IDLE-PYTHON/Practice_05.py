# Gerating the prime number
# 
def is_primes(num): 
    if num <= 1: 
        return False
    for i in range(2,int(num**0.5) + 1): 
        if num%i == 0: 
            return False
        return True
    

def genrate_prime_number(n): 
    prime_number = [ ]
    num = 2 
    while len(prime_number) < n:
        if is_primes(num):
            prime_number.append(num)
        num += 1 
    return prime_number
n = int(input("Enter the value of n: "))
prime_number = genrate_prime_number(n)
print(f"the first {n} prime numbers are {prime_number }")
    