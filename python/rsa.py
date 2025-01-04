import random
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(bitsize=8):
    while True:
        num = random.getrandbits(bitsize)
        if is_prime(num):
            return num

def generate_keys(bitsize=8):
    p = generate_prime(bitsize)
    q = generate_prime(bitsize)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(public_key, message):
    e, n = public_key
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    encrypted = pow(message_int, e, n)
    return encrypted

def decrypt(private_key, encrypted_message):
    d, n = private_key
    decrypted_int = pow(encrypted_message, d, n)
    decrypted_message = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return decrypted_message


def sign(private_key, message):
    d, n = private_key
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    signature = pow(message_int, d, n)
    return signature

def verify(public_key, message, signature):
    e, n = public_key
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    decrypted_signature = pow(signature, e, n)
    return message_int == decrypted_signature
