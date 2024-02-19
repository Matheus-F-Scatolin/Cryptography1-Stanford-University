import gmpy2

# Function to verify the factors
def verify_factors(N, p, q):
    return p * q == N

# Function to factorize N
def factorization(N):
    A = gmpy2.isqrt(N) + 1
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
    else:
        print("Factorization failed")

N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
factorization(N)