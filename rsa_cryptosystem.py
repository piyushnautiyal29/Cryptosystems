import sys
import random
import math

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

def lcm(a,b):
    return a*b//math.gcd(a,b)

def get_e(lambda_n):
    for e in range(2,lambda_n):
        if math.gcd(e,lambda_n)==1:
            return e
    return False

def get_d(e,lambda_n):
    for d in range(2,lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

floor = int(sys.argv[1])

# STEP 1: Choose 2 distinct prime numbers (p and q)
p=q=0
while True:
    p = get_prime(floor)
    q = get_prime(floor)
    if(p!=q):
        break
print("\n----STEP 1-------------")
print("Get 2 distinct prime numbers 'p' and 'q'")
print("'p'=",p)
print("'q'=",q)

# STEP 2: Compute n = p*q
n=p*q
print("\n----STEP 2-------------")
print("Get modulus(n) using 'p' and 'q'")
print("Using n=p*q, 'n'=",n)

# STEP 3: Compute λ(n)  =>      λ(n) = lcm(λ(p),λ(q))                 λ(p) = φ(p) = p − 1   and    λ(q) = q − 1
#                       So λ(n) = lcm((p - 1),(q - 1))
#   Since lcm(a,b) = |ab|/gcd(a,b)                          λ(n) = |(p - 1)(q - 1)|/gcd((p - 1),(q - 1))
lambda_n = lcm(p-1, q-1)
print("\n----STEP 3-------------")
print("Get Lambda of modulus using 'p' and 'q'")
print("Using λ(n) = lcm(p-1, q-1), 'λ(n)'=",lambda_n)

# STEP 4: Choose 'e' such that ==>>         1 < e < λ(n) and gcd(e, λ(n)) = 1
e = get_e(lambda_n)
print("\n----STEP 4-------------")
print("Get 'e' using Lambda calculated in step 3")
print("Using gcd(e, λ(n))=1, 'e'=",e)

# STEP 5: Solve 'd' for equation d⋅e ≡ 1 (mod λ(n))
d = get_d(e, lambda_n)
print("\n----STEP 5-------------")
print("Get 'd' using 1. 'e' from step 4 and 2. Lambda from step 3")
print("Using d*e ≡ 1 (mod λ(n)), 'd'=",d)

# PUBLIC AND PRIVATE KEYS GENERATED:
print("\n=====PUBLIC AND PRIVATE KEYS=========")
print("\nPUBLIC KEY (e,n) is (",e,",",n,")  ------------------------------  SEND PUBLIC KEY TO 'BOB'")
print("\nPRIVATE KEY (d,n) is (",d,",",n,") ------------------------------  KEEP PRIVATE KEY SECRET")
print("=======================================")

#   ENCRYPTION =>   ciphertext = plaintext**e mod n
#--------------ENCRYPTION-------------------------
print("\n----------'BOB' PC----------------")
print("BOB has 'e' and 'n'")
print("Encryption process => message^e mod n")
message = input("\nEnter a message to send : ")
message_stream = []
for char in message:
    char_to_ascii = ord(char)
    char_encrypt = char_to_ascii**e % n
    message_stream.append(char_encrypt)

print("\nGenerated encrypted message stream as following:")
print(message_stream)
print("\n============BOB SEND ABOVE STREAM TO ALICE=================")

#   DECRYPTION =>   plaintext = ciphertext**d mod n
#------------DECRYPTION----------------------------
print("\n-------------'ALICE' PC-----------------")
print("Alice has 'd' and 'n'")
print("Decryption process => cipher^d mod n")
print("\nRecieved message stream ",message_stream)

say = input("Decrypt Message? ")
if say == 'yes':
    plaintext = ""
    for item in message_stream:
        item_decrypt = item**d % n
        item_from_ascii_to_char = chr(item_decrypt)
        plaintext = plaintext + item_from_ascii_to_char

    print("\nAfter decrypting the message =",plaintext)
else:
    print("Not decrypting")
