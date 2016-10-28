import math
import random
import os

#TODO: performance! (cpython, exponentiation by squaring)
#TODO: write string functions
#TODO: toggle SAFE_PRIVATE_KEY_WRITE back to True
#TODO: remove globals

SAFE_PRIVATE_KEY_WRITE = False

#for ease of testing. Not good to have this in final version
GLOBAL_PRODUCT = 0
GLOBAL_EXPONENT = 0
GLOBAL_PRIVATE = 0

#given the n and exponent of a
def encrypt_int(m, n, e):
    return (m**e) % n

#given a message and the corresponding private key,
#decrypt it
def decrypt_int(c, private_key, n):
    return (c**private_key) % n

#encrypts and decrypts the given int, to test the functions
def test_int(m, n, e, d):
    print "Int test on", m
    encrypted = encrypt_int(m, n, e)
    print "Encrypted:", encrypted
    decrypted = decrypt_int(encrypted, d, n)
    if(decrypted == m):
        print "->Passed"
    else:
        print "->Failed"

#gets a coprime of n. A coprime is a value x such that the
#greatest common denominator between n and x is 1
#easiest way is to get a prime number and ensure
def get_coprime(n, primes):
    #3 is most common choice for e for some reason
    #so I check this first. I only use another number if
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
#the math behind this is honestly a bit of a black box to me
#this function would also probably need optimizing if you were using
#the full size of ints for a really secure implementation
def modular_mult_inverse(e, totient):
    nt = 1
    r = totient
    t = 0

    if totient < 0:
        totient = -totient;
    if e < 0:
        e = totient - (-e % totient)

    nr = e % totient
    while nr != 0:
        quot = r/nr | 0;
        temp = nt
        nt = t - quot*nt
        t = temp
        temp = nr
        nr = r - quot*nr
        r = temp

    if r > 1:
        return -1
    if t < 0:
        t += totient
    return t

#tells if an int n is prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#gets a random prime from the list of primes
def get_random_prime(primes):
    return random.choice(primes)

#reads in the primes from the local file "primes.txt",
#generated from generate_key.py
def read_primes():
    primes = []
    with open("primes.txt", "r") as in_file:
        for line in in_file:
            if line != '':
                primes.append(int(line.replace('\n', ''))) #strip \n
    return primes

#generates a public and private key, storing them in a file
#note that the primes generated in real RSA encryption are
#1024 bits long, to foil any reasonable attempt to factor them
def generate_key():
    #to be removed
    global GLOBAL_PRODUCT
    global GLOBAL_EXPONENT
    global GLOBAL_PRIVATE
    #

    primes = read_primes()
    prime1 = get_random_prime(primes)
    prime2 = get_random_prime(primes)
    n = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1) #phi, in the docs
    e = get_coprime(totient, primes)

    public_key = str(n) + "-" + str(e)
    private_key = modular_mult_inverse(e, totient)

    #also to be removed
    GLOBAL_PRODUCT = int(n)
    GLOBAL_EXPONENT = int(e)
    GLOBAL_PRIVATE = int(private_key)
    #

    print "Your public key:", public_key
    print "\nSend this out to the world!\nAnyone who wants to securely communicate with you will need to use it to encrypt their messages to you. "

    with open("public_key.txt", "w+") as out_file:
        out_file.write(str(public_key))
        out_file.write("\n")

    with open("private_key.txt", "w+") as out_file:
        out_file.write(str(private_key))
        out_file.write("\n")

    if(SAFE_PRIVATE_KEY_WRITE):
        os.chmod("private_key.txt", 0o400) #change permissions so only owner can read

    print "Your private key (used for decrypting messages to you) has been saved in ./private_key.txt"
    print "Do NOT share this key with anyone. Keep it hidden."


generate_key()
test_int(65, GLOBAL_PRODUCT, GLOBAL_EXPONENT, GLOBAL_PRIVATE)
