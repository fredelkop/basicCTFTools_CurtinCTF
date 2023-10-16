import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

p = 233970423115425145524320034830162017933
a = 0
b = 7
n = 233970423115425145498902418297807005944
Gx = 182
Gy = 85518893674295321206118380980485522083
Qx = 7856
Qy = 83120602848774683554512752392153815227

# The ciphertext you provided
cs = b'1JtwWPLfoVoUxK6TnRqyMIz00GldXbM0/dsaqBgWCO8hMlSRJITRknKVHhIGONYxgTBRyjIwIdVXn+ohLHBy2A=='

# Extract hte IV, ciphertext, and salt from the base64-encoded ciphertext
# Decode base64
decoded_cs = base64.b64decode(cs)

# Split into iv, ciphertext, and salt
iv = decoded_cs[:16]
ciphertext = decoded_cs[16:-16]
salt = decoded_cs[-16:]

# Calculate the encryption key using the same method
# Compute k
k = (Qx - Gx) * pow(Gy, -1, p) % p

# Compute key
key = scrypt(k.to_bytes((k.bit_length() + 7) // 8, 'big'), salt, 32, N=16384, r=8, p=1)

# Create an AES-CBC cipher
# Decrypt ciphertext
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Remove padding
padding_len = plaintext[-1]
plaintext = plaintext[:-padding_len]

print("Decrypted plaintext:", plaintext)
