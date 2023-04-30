from base64 import b64decode

FLAG1 = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
FLAG2 = 664813035583918006462745898431981286737635929725

flag = ""
flag += str(b64decode(FLAG1))
flag += str((FLAG2).to_bytes((FLAG2.bit_length() +7) // 8, 'big'))
print(flag)