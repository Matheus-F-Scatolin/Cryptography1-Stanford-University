import gmpy2

# Function to verify the factors
def verify_factors(N, p, q):
    return p * q == N

# Function to factorize N
def factorization(N):
    A = gmpy2.isqrt(24*N) + 1
    x = gmpy2.isqrt(A*A - 24*N)
    p = (A - x) // 6
    q = (A + x) // 4
    
    # If the factors are verified, print the factorization
    if verify_factors(N, p, q):
        print("Factorization successful:")
        print("N:", N)
        print("A:", A)
        print("x:", x)
        print("p:", p)
        print("q:", q)
    else:
        print("Factorization failed")

N = 720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929
factorization(N)