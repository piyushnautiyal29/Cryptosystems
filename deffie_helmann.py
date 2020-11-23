import sys
import random

def is_prime(number):
    for i in range(2, number):
        if(number%i==0):
            return False
        else:
            continue
    return True

def get_prime(floor):
    while True:
        p = random.randrange(floor, floor*2)
        if is_prime(p):
            return p

def is_generator(num, prime):
    for i in range(1, prime-1):
        if(num**i) % prime == 1:
            return False
    return True

def get_generator(prime):
    for num in range(2, prime):
        if is_generator(num, prime):
            return num

floor = int(sys.argv[1])
prime = get_prime(floor)
generator = get_generator(prime)
print("===============PUBLIC====================")
print("Deffie Helmann ( g , p ) values are (",generator,",",prime,")")

#Alice will do the following
alice_secret_num = random.randrange(40,100)
alice_text = (generator**alice_secret_num) % prime
print("\n\nAlice generate the following : ", alice_text)

#Bob will do the following
bob_secret_num = random.randrange(40,100)
bob_text = (generator**bob_secret_num) % prime
print("\n\nBob generate the following : ", bob_text)

#Alice global secret key generation
alice_global_key = (bob_text**alice_secret_num) % prime
print("\n\nAlice Key : ", alice_global_key)

#Bob global secret key generation
bob_global_key = (alice_text**bob_secret_num) % prime
print("\n\nBob Key : ", bob_global_key)
