from Crypto.Cipher import AES
from Crypto.Util import Counter

# This function decrypts a ciphertext using AES in CTR mode
def decrypt_ctr(key_hex, ciphertext_hex):
    # Convert the key and ciphertext from hexadecimal to bytes
    key = bytes.fromhex(key_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)

    # The nonce (IV) is the first 16 bytes of the ciphertext
    nonce = ciphertext[:16]

    # The rest is the actual encrypted message
    encrypted_message = ciphertext[16:]

    # Create a counter initialized with the nonce
    ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))

    # Create a new AES cipher object in CTR mode with our counter
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    # Decrypt the message and return it
    return cipher.decrypt(encrypted_message)

# Now you can use this function to decrypt your CTR ciphertexts
key = '36f18357be4dbd77f050515c73fcf9f2'
ciphertext1 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
ciphertext2 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'

print(decrypt_ctr(key, ciphertext1).decode())
print(decrypt_ctr(key, ciphertext2).decode())
