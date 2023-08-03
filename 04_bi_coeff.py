# dp pascal's triangle unusable due to time/space complexity
# >>> Fermat's Little Theorem (FLT)!

# If "p" is a prime number and "a" is an integer not divisible by "p"
# then (a^(p-1)) % p = 1.

# modular inverse:
# for int 'a' and prime number 'p', modular inverse of 'a' modulo 'p' is:
# an integer x such that (a * x) % p = 1

# 1,000,00,007 is a widely used prime modulus >>> a prime number!

MOD = 1000000007  # prime modulo given!

def factorial_mod(n):
    result = 1
    for i in range(1, n+1):
        result = (result*i) % MOD
    return result

def bi_coeff(n, k):
    # make! it! smaller!
    if k > n-k:
        k = n-k

    # modulo arithmetic is not distributive over division.
    # changing division to multiplication via FLT is necessary.

    # numer = n! % MOD
    # denom = (k! % MOD) * ((n-k)! % MOD) % MOD
    numer = factorial_mod(n)
    denom = (factorial_mod(k) * factorial_mod(n-k)) % MOD

    # modular inverse via FLT: pow(x, p-2, p)
    inv_denom = pow(denom, MOD-2, MOD)

    # multiplying by the modular inverse of a number
    # is equivalent to dividing by that number modulo MOD
    # OR:
    # inv_demnom is congruent to (1/denom) % MOD
    # and multiplying congruences and taking modulo are equivalent operations
    print((numer * inv_denom) % MOD)

N, K = map(int, input().split())
bi_coeff(N, K)

