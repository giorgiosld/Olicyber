ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
plaintext = ""

def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x^y for x,y in zip(a,b)])

for o in range(256):
    plaintext = xor(bytes.fromhex(ciphertext), o.to_bytes(1, "big")*25)
    if plaintext.isascii():
        print(str(hex(o)))
        print('flag{' + str(plaintext) + '}')

#found that the key is strgit "0x20"*25 so "20"*25
print('flag{' + str(xor(bytes.fromhex(ciphertext), bytes.fromhex("20"*25))) + '}')