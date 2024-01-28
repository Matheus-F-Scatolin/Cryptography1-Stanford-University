from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

# This function encrypts a plaintext using AES in CTR mode
def encrypt_ctr(key_hex, plaintext):
    # Convert the key from hexadecimal to bytes
    key = bytes.fromhex(key_hex)

    # Generate a random nonce
    nonce = get_random_bytes(16)

    # Create a counter initialized with the nonce
    ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))

    # Create a new AES cipher object in CTR mode with our counter
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    # Encrypt the plaintext and return the nonce concatenated with the ciphertext
    return nonce + cipher.encrypt(plaintext.encode())

# Now you can use this function to encrypt your plaintexts
key = '36f18357be4dbd77f050515c73fcf9f2'
plaintext = 'This is another test message.'

print(encrypt_ctr(key, plaintext).hex())
