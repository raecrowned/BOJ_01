import sys
input = sys.stdin.readline
MOD = 1000  # for modulo!

def matrix_mult(mat1, mat2):
    retval = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                retval[i][j] = (retval[i][j] + (mat1[i][k] * mat2[k][j])) % MOD
    return retval

def matrix_selfmult(mat):
    retval = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                retval[i][j] = (retval[i][j] + (mat[i][k] * mat[k][j])) % MOD
    return retval

# divide-and-conquer:
# A^(2k) = (A^k)^2, for matrix exponentials
def matrix_pow(mat, exp):
    if exp == 1:
        return mat
    half_pow = matrix_pow(mat, exp//2)  # rounds off if exp is odd; take care of it in 'else'
    if exp % 2 == 0:
        return matrix_selfmult(half_pow)
    else:
        return matrix_mult(mat, matrix_selfmult(half_pow))

# global
n, b = map(int, input().split())

# iterators are "streamlined results" made into a datatype; functionally, it is not exactly an object in the traditional sense

# list comprehension w/ unpacking operator '*'
matrix =[[*map(int, input().split())]for _ in range(n)]
matrix = [[element % MOD for element in row] for row in matrix]
result = matrix_pow(matrix, b)

# print here
for i in range(n):
    for j in range(n):
        sys.stdout.write(str(result[i][j]) + " ")
    sys.stdout.write("\n")
