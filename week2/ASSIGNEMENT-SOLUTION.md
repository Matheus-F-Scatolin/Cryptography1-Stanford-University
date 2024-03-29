# AES Encryption/Decryption Assignment

This repository contains the code used to solve an assignment on implementing AES encryption and decryption in both CBC and CTR modes.

## ASIGNEMENT

In this project, you will implement two encryption/decryption systems, one using AES in CBC mode and another using AES in counter mode (CTR). In both cases, the 16-byte encryption IV is chosen at random and is prepended to the ciphertext.

For CBC encryption, we use the PKCS5 padding scheme discussed in the lecture (L14:44). While we ask that you implement both encryption and decryption, we will only test the decryption function. In the following questions, you are given an AES key and a ciphertext (both are hex encoded) and your goal is to recover the plaintext and enter it in the input boxes provided below.

For implementation purposes, use any existing crypto library such as PyCrypto (Python), Crypto++ (C++), or any other. While it is fine to use built-in AES functions, we ask that as a learning experience you implement CBC and CTR mode yourself.

Question 1

CBC key: 140b41b22a29beb4061bda66b6747e14

CBC Ciphertext 1: 4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c10da98ab1f8649f85

Answer: CBC mode encryption needs padding.

CBC key: 140b41b22a29beb4061bda66b6747e14

CBC Ciphertext 2: 5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253

Answer: Our implementation uses rand. IV.

Question 3

CTR key: 36f18357be4dbd77f050515c73fcf9f2

CTR Ciphertext 1: 69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329

Answer: CTR mode lets you build a stream cipher from a block cipher.

Question 4

CTR key: 36f18357be4dbd77f050515c73fcf9f2

CTR Ciphertext 2: 770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451

Answer: Always avoid the two time pad!

## Files in this Repository

1. `decrypt_aes_cbc.py`: This Python script contains the function `decrypt_cbc` which takes a hexadecimal key and a hexadecimal ciphertext as input, and returns the decrypted plaintext. The function uses the PyCrypto library to perform AES decryption in CBC mode.

2. `decrypt_aes_ctr.py`: This Python script contains the function `decrypt_ctr` which takes a hexadecimal key and a hexadecimal ciphertext as input, and returns the decrypted plaintext. The function uses the PyCrypto library to perform AES decryption in CTR mode.

3. `encrypt_aes_cbc.py`: This Python script contains the function `encrypt_cbc` which takes a hexadecimal key and a plaintext message as input, and returns the encrypted ciphertext in hexadecimal format. The function uses the PyCrypto library to perform AES encryption in CBC mode.

4. `encrypt_aes_ctr.py`: This Python script contains the function `encrypt_ctr` which takes a hexadecimal key and a plaintext message as input, and returns the encrypted ciphertext in hexadecimal format. The function uses the PyCrypto library to perform AES encryption in CTR mode.

## Steps to Solve the Assignment

1. I implemented the decryption functions for both CBC and CTR modes in the `decrypt_aes_cbc.py` and `decrypt_aes_ctr.py` files respectively. I tested these functions with the provided ciphertexts and keys.

2. After successfully decrypting the ciphertexts, I moved on to implement the encryption functions for both CBC and CTR modes in the `encrypt_aes_cbc.py` and `encrypt_aes_ctr.py` files respectively.

3. I tested the encryption functions with various plaintexts and keys to ensure they were working correctly.

4. Finally, I documented all the steps and the purpose of each file in this file.
