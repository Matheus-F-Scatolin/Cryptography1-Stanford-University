# Weekly Programming Challenges - Crypto Course

This repository contains my solutions to the weekly programming challenges for the [Cryptography I Course](https://www.coursera.org/learn/crypto) created by Stanford University and offered by Unicamp on Coursera.

## 📜 Table of Contents

- [📖 Course Link](#-course-link)
- [🛠️ How to Use This Repository](#️-how-to-use-this-repository)
- [📂 Structure of the Repository](#-structure-of-the-repository)
  - [🗓️ Week 1](#️-week-1)
  - [🗓️ Week 2](#️-week-2)
  - [🗓️ Week 3](#️-week-3)
  - [🗓️ Week 4](#️-week-4)
  - [🗓️ Week 5](#️-week-5)
  - [🗓️ Week 6](#️-week-6)

## 📖 Course Link

This repository contains my solutions for the [Cryptography I Course](https://www.coursera.org/learn/crypto) by Stanford University, offered on Coursera.

## 🛠️ How to Use This Repository

This repository hosts my personal solutions and notes for the weekly programming challenges in the Coursera Cryptography I course. You can use it as a reference to compare different approaches, gain insights into specific solutions, or refresh your understanding of the concepts covered. To maximize your learning, I encourage you to attempt the challenges on your own first!

## 📂 Structure of the Repository

The repository is organized with one directory for each week's challenges. Inside each directory, you'll find Python scripts that solve the challenge, along with a 'ASSIGNMENT-SOLUTION' file that explains my approach.

### 🗓️ Week 1

Contains files related to an assignment on breaking a stream cipher when the key is reused (Many Time Pad attack).

- 📜 `ASSIGNMENT-SOLUTION.md`: Explains the assignment and the methodology to decrypt the target ciphertext.
- 🐍 `Discovering_each_letter.py`: Python script used to XOR ciphertexts and convert results to ASCII, aiding in the decryption of the target message.
- 🐍 `spaces_matrix.py`: Python script to build a matrix by XORing all ciphertexts with each other, used to identify likely space positions in the plaintexts.
- 📄 `spaces_per_ct.txt`: Text file, likely an output, containing identified space positions for each ciphertext and the final decrypted message.
- 🐍 `testing_spaces.py`: Python script to identify common space positions across multiple ciphertexts by analyzing the output of `spaces_matrix.py`.

### 🗓️ Week 2

Contains scripts for implementing AES encryption and decryption in both CBC and CTR modes.

- 🐍 `decrypt_aes_cbc.py`: Decrypts a given ciphertext using AES in CBC mode.
- 🐍 `decrypt_aes_ctr.py`: Decrypts a given ciphertext using AES in CTR mode.
- 🐍 `encrypt_aes_cbc.py`: Encrypts a given plaintext using AES in CBC mode.
- 🐍 `encrypt_aes_ctr.py`: Encrypts a given plaintext using AES in CTR mode.

### 🗓️ Week 3

Focuses on building a file authentication system using chained hashes, enabling browsers to authenticate and play video chunks as they download.

- 📜 `ASSIGNMENT.md`: Describes the assignment, the chained hashing mechanism, and provides challenge/example files.
- 🎬 `challenge.mp4_download`: The primary video file for the assignment.
- 🎬 `example.mp4_download`: An example video file with a known root hash for testing the implementation.
- 🖼️ `image.png`: A diagram illustrating the chained hashing process for file blocks.
- 🐍 `solution.py`: Python script that implements the chained hashing algorithm to compute the root hash (`h_0`) of a given file.

### 🗓️ Week 4

Revolves around a padding oracle attack against a web server.

- 📜 `ASSIGNMENT.md`: Details the assignment, explaining how to use server error codes (403 for bad padding, 404 for good padding but malformed message) to decrypt a ciphertext.
- 🐍 `padding_oracle.py`: Python script containing the `PaddingOracle` class, which sends manipulated ciphertexts to the target server and returns whether the padding was valid.
- 🐍 `solution.py`: Python script that implements the logic for the padding oracle attack to decrypt the target ciphertext byte by byte. The successfully decrypted message is included as a comment.

### 🗓️ Week 5

Covers the Meet-in-the-Middle attack to solve a discrete logarithm problem.

- 📜 `ASSIGNMENT.md`: Describes the assignment to find `x` in `h = g^x mod p` using the meet-in-the-middle technique. Provides the values for `p`, `g`, and `h`.
- 🐍 `meet-in-the-middle.py`: Python script implementing the meet-in-the-middle algorithm. It uses `gmpy2` for handling large number arithmetic.

### 🗓️ Week 6

Addresses RSA vulnerabilities when prime factors `p` and `q` of the modulus `N` are improperly generated (e.g., too close).

- 📜 `ASSIGNMENT.md`: Explains the theoretical background and presents four factoring challenges, including one decryption task using a factored modulus.
- 🐍 `factoring_challenge1.py`: Python script for factoring `N` when `|p-q| < 2N^(1/4)`.
- 🐍 `factoring_challenge2.py`: Python script for factoring `N` when `|p-q| < 2^11 * N^(1/4)`, which may require iterating to find the correct arithmetic mean `A`.
- 🐍 `factoring_challenge3.py`: Python script for factoring `N` when `|3p-2q| < N^(1/4)`, requiring an adapted factoring method.
- 🐍 `factoring_challenge4.py`: Python script that uses the factorization from Challenge 1 to decrypt an RSA-encrypted message, including handling PKCS#1 v1.5 padding.
