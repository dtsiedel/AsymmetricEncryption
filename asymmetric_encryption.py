import math
import random

#gets a coprime of n. A coprime is a value x such that the
#greatest common denominator between n and x is 1
def get_coprime(n):
    pass

#tells if an int n is prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#gets a random prime from the list of primes
def get_random_prime(primes):
    return random.choice(primes)

#generates a public and private key, storing them in a file
#note that the primes generated in real RSA encryption are
#1024 bits long, to foil any reasonable attempt to factor them
def generate_key():
    primes = [x for x in range(2,1000000) if is_prime(x)]
    prime1 = get_random_prime(primes)
    prime2 = get_random_prime(primes)
    n = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1) #phi, in the docs
    e = get_coprime(totient)


    public_key = str(n) + "-" + str(e)
    #private_key = ...

generate_key()
