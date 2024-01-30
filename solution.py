from Crypto.Hash import SHA256

# This function finds the last 1024-byte block of the file.
def find_last_block(file_path):
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Go to the end of the file 
        # seek(0, 2) means we want to go to the first position starting from the end of the file
        file.seek(0, 2)

        # Get the current position of the file pointer (i.e., the file size)
        file_size = file.tell()

        # Calculate the position of the start of the last 1024-byte block
        start_of_last_block = file_size - (file_size % 1024)

        # Go to the start of the last block
        file.seek(start_of_last_block)

        # Read from the start of the last block to the end of the file
        binary_data = file.read()

        # Now `binary_data` contains the last block of the file
        return binary_data, start_of_last_block

# This function finds the previous 1024-byte block and appends the current hash to it.
def find_previous_block(file, current_position, current_hash):
    # Go to the start of the new block
    file.seek(current_position)

    # Read the block
    new_block = file.read(1024)

    # Convert the binary string back to bytes
    current_hash_bytes = bytes(int(current_hash[i:i+8], 2) for i in range(0, len(current_hash), 8))

    # Add the current hash as a sufix to the block
    new_block = new_block + current_hash_bytes

    return new_block

# This function calculates the SHA-256 hash of a block of data and returns it as a binary string.
def sha256_hashing(message):
    # Create a new SHA-256 hash object
    hash_object = SHA256.new()

    # Update the hash object with the message.
    hash_object.update(message)

    # Get the hexadecimal digest of the message.
    hex_digest = hash_object.hexdigest()

    # Convert to binary, remove the '0b' prefix, and fill with zeros if necessary
    binary_digest = bin(int(hex_digest, 16))[2:].zfill(256)
    return binary_digest


def main():
    # Initialize the first block with the end of the file
    current_block, current_position = find_last_block('challenge.mp4_download')

    #calculate the last block's hash
    current_hash = sha256_hashing(current_block)

    #create a loop to go through all blocks
    with open('challenge.mp4_download', 'rb') as file:
        while True:
            #update the current position
            current_position -= 1024

            # Make the current block the block previous to it
            current_block = find_previous_block(file, current_position, current_hash)

            # Calculate the new hash
            current_hash = sha256_hashing(current_block)

            #if the current position is 0, the beggining of the file has been reached
            if current_position == 0:
                break

    # Convert the binary hash to hexadecimal and print it.
    hex_hash = hex(int(current_hash, 2))[2:].zfill(64)
    print(hex_hash)


if __name__ == '__main__':
    main()

'''This code reads a file in reverse, 1024 bytes at a time, and calculates the SHA-256 hash of each block.
It then appends the hash of each block to the next block, and calculates the hash of the combined data.
This process is repeated until the beginning of the file is reached. The final output is the SHA-256 hash
of the first block of the file, represented as a hexadecimal string.'''