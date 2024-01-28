from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# This function encrypts a plaintext using AES in CBC mode
def encrypt_cbc(key_hex, plaintext):
    # Convert the key from hexadecimal to bytes
    key = bytes.fromhex(key_hex)

    # Generate a random IV
    iv = get_random_bytes(16)

    # Create a new AES cipher object in CBC mode with our IV
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Pad the plaintext, encrypt it and return the IV concatenated with the ciphertext
    return iv + cipher.encrypt(pad(plaintext.encode(), AES.block_size))

# Now you can use this function to encrypt your plaintexts
key = '140b41b22a29beb4061bda66b6747e14'
plaintext = 'This is a test message.'

print(encrypt_cbc(key, plaintext).hex())
