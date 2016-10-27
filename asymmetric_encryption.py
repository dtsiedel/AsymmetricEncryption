import math
import random

#TODO: implementation for getting private key
#TODO: write private_key to file, public_key to stdout
#TODO: encrypt/decrypt functions, so you can actually use it for something

#TODO: move primes to a file, to read in instead of always recomputing

#gets a coprime of n. A coprime is a value x such that the
#greatest common denominator between n and x is 1
#easiest way is to get a prime number and ensure
def get_coprime(n, primes):
    #3 is most common choice for e for some reason
    #so i check this first. I only use another number if
    #3 is not coprime with n

    #my assumption is that it is best to use a small number
    #like 3 for the sake of computational speed
    if n % 3 != 0:
        return 3

    for prime in primes:
        if n % prime != 0:
            return prime

#calculates d, the modular multiplicative inverse of e(mod(totient))
#this will be the private key needed to decrypt messages 
def modular_mult_inverse(e, totient):
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
    e = get_coprime(totient, primes)

    public_key = str(n) + "-" + str(e)
    private_key = modular_mult_inverse(e, totient)

    print "Your public key:", public_key
    print "\nSend this out to the world!\nAnyone who wants to securely communicate with you will need to use it to encrypt their messages to you. "

generate_key()
