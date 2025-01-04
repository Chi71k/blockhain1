K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0x5b8f7e13, 0x6c44198c, 0x4a475817, 0x687c1dbb, 0x16e70352, 0x3ac97511, 0x93dd08f7,
    0x6c44a1e1, 0x24d01d68, 0xe8f5f40f, 0x28c7d0ab, 0x39baae80, 0x0b6707a2, 0x41ce28e2, 0x97c6a2f9,
    0x63b91e8d, 0x37634e36, 0x0f64b392, 0x6874b6ff, 0x6c43f897, 0x6d572021, 0x0c7a3a28, 0x4c80a5dd,
    0x279c49c5, 0x7f7e2a4b, 0x1d4b5225, 0x032beaa9, 0x214f22dd, 0x110fd0f6, 0x0fa3f510, 0x7035bff7,
    0x4cf6ed43, 0x34d91899, 0x56f7b206, 0x0b9a6e1f, 0x3f5f8b96, 0x78d119de, 0x7fbb0eb4, 0x7c5403d4,
    0x6ef96fd8, 0x41ccdb84, 0x232b8d97, 0x7754d1d3, 0x5efc199d, 0x285b0737, 0x602f0e72, 0x1cc5d0d7
]

def right_rotate(val, bits):
    return (val >> bits) | (val << (32 - bits)) & 0xffffffff

def pad_message(msg):
    if isinstance(msg, str):  # Check if msg is a string
        msg = msg.encode('utf-8')
    original_len = len(msg) * 8
    msg += b'\x80'
    while len(msg) % 64 != 56:
        msg += b'\x00'
    msg += original_len.to_bytes(8, 'big')
    return msg

def hash(msg):
    msg = pad_message(msg)
    hash_values = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    for i in range(0, len(msg), 64):
        block = msg[i:i + 64]
        w = [0] * 64
        for j in range(16):
            w[j] = int.from_bytes(block[j * 4:j * 4 + 4], 'big')
        for j in range(16, 64):
            s0 = right_rotate(w[j - 15], 7) ^ right_rotate(w[j - 15], 18) ^ (w[j - 15] >> 3)
            s1 = right_rotate(w[j - 2], 17) ^ right_rotate(w[j - 2], 19) ^ (w[j - 2] >> 10)
            w[j] = w[j - 16] + s0 + w[j - 7] + s1
            w[j] &= 0xffffffff

        a, b, c, d, e, f, g, h = hash_values

        for j in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ (~e & g)
            temp1 = h + S1 + ch + K[j] + w[j]
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = S0 + maj

            h = g
            g = f
            f = e
            e = d + temp1
            d = c
            c = b
            b = a
            a = temp1 + temp2

        hash_values = [(x + y) & 0xffffffff for x, y in zip(hash_values, [a, b, c, d, e, f, g, h])]

    return ''.join(f'{x:08x}' for x in hash_values)
