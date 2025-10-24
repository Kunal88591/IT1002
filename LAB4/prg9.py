# WAP: Prime numbers up to n using function

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")

n = int(input("Enter limit: "))
print(f"Prime numbers up to {n}:")
print_primes(n)
