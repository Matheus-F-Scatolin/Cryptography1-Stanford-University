'''When the server responds with error 404, That means the padding is correct.
Then, the last decrypted byte is 0x01. Thus, the last byte of the plaintext is
0x01 xor i. We can then repeat this process to decrypt the rest of the bytes, xoring
i with the hexadecimal representation of the number of the current byte from the end
(2, 3, 4, etc).
Note that after we find out the last byte, the correct padding will be 0x02 0x02,
which means we have to xor the last byte with 0x02, then the two last bytes with 0x03,
the three last bytes with 0x04 and so on, repeating this after the discovery of each
byte until the whole block is decrypted.
Then we can just repeat this to tthe prior blocks, until the whole message is decrypted.

Solution: The message is "The Magic Words are Squeamish Ossifrage"'''

from padding_oracle import PaddingOracle

TARGET = 'http://crypto-class.appspot.com/po?er='

def main():
    po = PaddingOracle()
    current_arg = ''
    original_arg = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4' # Choose the argument to be sent to the server

    #find out the last byte of the last block:
    for i in range(0, 256):
        current_arg = original_arg[:94] + format(i, '02x') + original_arg[96:]
        if po.query(current_arg):
            print(f"Last byte: {format(i, '02x')}")
            break

if __name__ == "__main__":
    main()