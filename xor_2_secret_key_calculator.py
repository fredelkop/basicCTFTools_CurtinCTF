def reverse_obfuscate_key(obfuscated_key):
    obfuscated_key_bytes = obfuscated_key.to_bytes((obfuscated_key.bit_length() + 7) // 8, byteorder='big')
    original_key_bytes = bytes([x ^ 0xFF for x in obfuscated_key_bytes])
    original_key = int.from_bytes(original_key_bytes, byteorder='big')
    return original_key

# Replace the obfuscated key and ciphertext with your actual values
obfuscated_alice_key = 9 # Replace with the actual obfuscated key
encrypted_flag = 7091022811630043496454715564459978004849567585581799855855165734358

# Reverse obfuscated to get the shared key
alice_shared_key = reverse_obfuscate_key(obfuscated_alice_key)

# Decrypt the ciphertext
decrypted_flag_bytes = encrypted_flag ^ alice_shared_key

# Convert the decrypted bytes back to a string
decrypted_flag = decrypted_flag_bytes.to_bytes((decrypted_flag_bytes.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

# Print the decrypted plaintext
print(f"Decrypted Flag: {decrypted_flag}")