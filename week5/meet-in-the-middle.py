# Meet in the middle attack
# (h/g^x1) % p = ((g^b)^x0) % p
import gmpy2

#  Constants
B = gmpy2.mpz(2**20)
H = gmpy2.mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')
G = gmpy2.mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
P = gmpy2.mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')

# calculates (h/g^x1) mod p - the left side of the equation
def left(x, p, g, h):
    gx = gmpy2.powmod(g, x, p) # Precompute g^x
    return gmpy2.divm(h, gx, p)

# calculates ((g^b)^x0) mod p - the right side of the equation
def right(x, p, gB):
    return gmpy2.powmod(gB, x, p)

# Takes a prime p, a generator g and an element h and prints x such that g^x = h mod p
def discrete_log(p, g, h):
    #  First build a hash table (dictionary) of all possible values of the left hand side (LEFT(x1):x1)
    hash_table = {}
    print("Building hash table...")
    for x1 in range(0, B):
        #  Print progress
        if x1 % 80000 == 0:
            print(f"{x1 / B * 100:.2f}%")

        hash_table[left(x1, p, g, h)] = x1
    print("100%")
    print("Hash table built.")

    #  Then iterate over all possible values of the right hand side (RIGHT(x0)) and check if it is in the hash table
    gB = gmpy2.powmod(g, B, p) # Precompute g^B
    for x0 in range(B):
        if hash_table.get(right(x0, p, gB)) != None:
            # If it is, we have found a match
            x1 = hash_table[right(x0, p, gB)]
            print(f"Found x0: {x0}, x1: {x1}.")
            print(f"Which means: x = {x0*B + x1}.")
            print(f"Check: {gmpy2.powmod(g, x0*B + x1, p) == h}")
            break

def main():
    discrete_log(P, G, H)
    print("Done!")

if __name__ == "__main__":
    main()
