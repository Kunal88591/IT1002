# write a recursive function to check wheather a number can be expressed as a sum of two prime number 

def is_prime(n, d=2):
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)

def check_sum_of_primes(n, p=2):
    if p > n // 2:
        return False
    if is_prime(p) and is_prime(n - p):
        return True
    return check_sum_of_primes(n, p + 1)

num = int(input())
print(check_sum_of_primes(num))
