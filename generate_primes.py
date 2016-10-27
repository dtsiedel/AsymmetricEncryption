import math

#tells if an int n is prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primes = [x for x in range(2,1000000) if is_prime(x)]


with open("primes.txt", "w") as out_file:
    for prime in primes:
        out_file.write(str(prime) + "\n")
