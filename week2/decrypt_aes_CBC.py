from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# This function decrypts a ciphertext using AES in CBC mode
def decrypt_cbc(key_hex, ciphertext_hex):
    # Convert the key and ciphertext from hexadecimal to bytes
    key = bytes.fromhex(key_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)

    # The IV is the first 16 bytes of the ciphertext
    iv = ciphertext[:16]

    # The rest is the actual encrypted message
    encrypted_message = ciphertext[16:]

    # Create a new AES cipher object in CBC mode with our IV
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)

    # Decrypt the message, unpad it and return it
    return unpad(cipher.decrypt(encrypted_message), AES.block_size)

# Now you can use this function to decrypt your CBC ciphertexts
key = '140b41b22a29beb4061bda66b6747e14'
ciphertext1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
ciphertext2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'

print(decrypt_cbc(key, ciphertext1).decode())
print(decrypt_cbc(key, ciphertext2).decode())
