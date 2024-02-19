import gmpy2

# Function to verify if the factors are correct
def verify_factors(N, p, q):
    return p * q == N

# Function to factorize N
def factorization(N):
    sqrtN = gmpy2.isqrt(N) + 1
    # Iterate over the range of A values
    for i in range (sqrtN, sqrtN + 2**20):
        A = i
        x = gmpy2.isqrt(A*A - N)
        p = A - x
        q = A + x
        # If the factors are verified, print the factorization
        if verify_factors(N, p, q):
            print("Factorization successful:")
            print("N:", N)
            print("A:", A)
            print("x:", x)
            print("p:", p)
            print("q:", q)
            break

N = 648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877
factorization(N)