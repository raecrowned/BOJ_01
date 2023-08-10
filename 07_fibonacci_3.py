import sys
input = sys.stdin.readline

MOD = 1000000
MAT = [[1, 1], [1, 0]]
FIB = [[1, 0], [0, 1]]

# general fibonnaci formula using linear algebra:
# [[1, 1],  ^ n  == [[F_next, F_curr],
#  [1, 0]]           [F_curr, F_prev]]

# get a reverse-binary array of n
def rev_binary(n):
    rev_biarr = []
    while n > 0:
        rem = n % 2
        n = n // 2
        rev_biarr.append(rem)
    return rev_biarr

# matrix multiplication w/ modulo
def matmul2_2(a, b):
    retmat = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                retmat[i][j] += a[i][k] * b[k][j]
                retmat[i][j] %= MOD
    return retmat

def fibonacci(n):
    if n == 1:              # n starts at 1
        return 1

    rev_biarr = rev_binary(n)
    rev_len = len(rev_biarr)

    # tmp stores binary-exp tmp matrices
    # fin calculates the full thing
    tmp, fib = [MAT], FIB

    # 2-exponents of MAT for quick-mult
    for i in range(1, rev_len):
        tmp.append(matmul2_2(tmp[-1], tmp[-1]))

    # quick-mult; if rev_biarr[i], tmp[i] is multiplied to base.
    for i in range(rev_len):
        if rev_biarr[i]:
            fib = matmul2_2(fib, tmp[i])
    return fib[0][1]        # fib_curr at [0][1]

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
