from Crypto.Cipher import AES
import base64

def pkcs7_unpad(data):
    padding = data[-1]
    return data[:-padding]
#0,1,2,4
def b_p(data):
    l = [4, 1, 3, 0, 2, 7, 6, 5, 10, 9, 8, 11, 15, 14, 13, 12, 19, 18, 17, 16, 23, 22, 21, 20, 27, 26, 25, 24, 31, 30, 29, 28]
    y = bytearray(32)
    for i, index in enumerate(l):
        if i < len(data):
            y[index] = data[i]
    return bytes(y)

with open('challenge_file.txt', 'r') as file:
    ctn = base64.b64decode(file.read())
    
iv = b'\x00' * 16
cn = AES.new(iv, AES.MODE_CBC, iv)

# Decrypt the ciphertext and remove padding
k = cn.decrypt(ctn)
fp = pkcs7_unpad(k)

#Initialize the AES cipher in ECB mode
c = AES.new(iv, AES.MODE_ECB)

flag = c.decrypt(fp)
# Revert the byte order
flag = b_p(flag)
print("Decoded Flag:")
print(flag.decode('utf-8'))
    