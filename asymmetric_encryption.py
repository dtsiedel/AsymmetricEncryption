import math

#tells if an int n is prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#gets a random prime from the list of primes
def get_random_prime(primes):
    #generate random number in range
    #get number at that index and return it
    pass

#generates a public and private key, storing them in a file
def generate_key():
    primes = [x for x in range(0,1000000) if is_prime(x)]
    print primes
    num1 = get_random_prime(primes)
    num2 = get_random_prime(primes)


generate_key()
