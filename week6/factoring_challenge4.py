import gmpy2

# Function to verify if the factors are correct
def verify_factors(N, p, q):
    return p * q == N

# Function to factorize N
def factorization(N):
    A = gmpy2.isqrt(N) + 1
    x = gmpy2.isqrt(A*A - N)
    p = A - x
    q = A + x

    # If the factors are verified, return the factorization
    if verify_factors(N, p, q):
        return (p, q)
    else:
        print("Factorization failed")

N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
e = 65537
ciphertext = 22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540
# factorate N
p, q = factorization(N)

# calculate d
phi_N = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_N)

# apply RSA decryption (elevate the ciphertext to the power of d modulo N)
decripted_ciphertext = gmpy2.powmod(ciphertext, d, N)
hex_dec_ciphertext = hex(decripted_ciphertext)

if hex_dec_ciphertext.startswith("0x2"):
    # Find the first "00" in the hex representation of the decrypted ciphertext (this is where the random padding ends and the message starts)
    start = hex_dec_ciphertext.index("00") + 2
    hex_msg = hex_dec_ciphertext[start:]
    # Convert the hex message to ASCII
    print(bytes.fromhex(hex_msg).decode('ascii'))
