from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
import hashlib

cipher_text = 32411595437849678646243211671030544758585858507474463678322444828159706619638328084506795350455714014545653039715173
x = 11109871761272186707313749920559391609314864049943716089329850308739848274981163174574586779728080951298251641374993669445207041118824097375920261081696413

# Calculate the private key 'a' using the given ciphertext and x
B = 11
a = 0
while True:
    key = hashlib.md5(long_to_bytes(pow(B, a, x))).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(long_to_bytes(cipher_text))
    
    # Check of the last bytes represents the padding length
    if decrypted_data[-decrypted_data[-1]:] == bytes([decrypted_data[-1]] * decrypted_data[-1]):
        break
    
    a += 1
    
# Remove the PKCS7 padding
plain_text = decrypted_data[:-decrypted_data[-1]]
print("Decrypted flag: ", plain_text.decode('utf-8'))