# This script identifies positions in a list of ciphertexts that likely contain spaces. 
# Given the matrix of a certain ciphertext, it outputs the likely positions in this ciphertext where there are spaces.

# 'matrix' is a list of lists, where each sublist represents a ciphertext.
# Each number in a sublist represents a position in the ciphertext where ther is a space.
matrix = [[2, 3, 6, 10, 13, 17, 18, 21, 22, 24, 25, 32, 33, 35, 40, 42, 51, 54, 56, 58, 60, 63, 64, 68, 70, 73, 74, 78, 81, 82, 86, 88, 89, 96, 104, 114, 133],
[3, 5, 10, 11, 18, 20, 22, 26, 27, 31, 33, 39, 42, 47, 49, 50, 55, 56, 57, 60, 68, 70, 78, 80, 81, 82, 83, 86, 88], 
[8, 10, 14, 18, 20, 22, 27, 28, 31, 33, 38, 42, 49, 50, 53, 56, 57, 60, 63, 64, 65, 68, 69, 72, 73, 89], 
[10, 14, 18, 22, 26, 27, 28, 35, 42, 44, 50, 54, 56, 63, 64, 71, 73, 78, 82, 86, 88, 95, 104, 118, 129, 134], 
[7, 9, 10, 14, 17, 18, 22, 30, 33, 34, 35, 39, 42, 44, 46, 49, 54, 56, 60, 64, 66, 68, 69, 73, 88, 104], 
[3, 5, 9, 10, 13, 18, 19, 27, 33, 37, 48, 50, 53, 56, 58, 60, 64, 66, 68, 71, 73, 76, 78, 81, 86, 104, 105, 114, 118], 
[3, 5, 9, 10, 13, 18, 19, 27, 33, 39, 42, 44, 50, 51, 55, 60, 64, 66, 68, 69, 78, 79, 86, 95, 96, 114, 118, 130, 160, 168], 
[2, 3, 6, 14, 18, 20, 21, 22, 26, 27, 30, 33, 38, 42, 46, 50, 51, 56, 57, 60, 61, 68, 69, 78, 82, 88, 95, 96, 104, 115, 118, 121], 
[1, 2, 3, 14, 15, 16, 18, 21, 22, 33, 34, 35, 41, 43, 49, 50, 54, 55, 56, 60, 62, 68, 73, 74, 86, 88, 89, 96, 104, 114], 
[3, 4, 10, 12, 18, 21, 22, 27, 29, 30, 32, 34, 36, 42, 45, 50, 52, 55, 56, 59, 60, 63, 64, 66, 67, 68, 73, 75, 77, 78, 79, 86, 88]]

# 'pos_spaces' will store the positions that likely contain spaces.
pos_spaces = []

# This function counts the occurrences of a given number (position) in all sublists of 'matrix'.
def count_appearances(number):
    counter = 0
    for list in matrix:
        if number in list:
            counter += 1
    return counter

# For each position in the first three ciphertexts, count its occurrences in all ciphertexts.
# If a position appears in at least 7 ciphertexts, it likely contains a space.
for xored_ct in range(3):
    for pos in matrix[xored_ct]:
        counter = count_appearances(pos)
        if counter >= 7:
            pos_spaces.append(pos)

# Print out the sorted, unique positions that likely contain spaces.
print(sorted(list(set(pos_spaces))))
