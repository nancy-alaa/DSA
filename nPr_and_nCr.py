import math

# number of Permutations
def nPr(n, r):
    return 0 if r > n else math.factorial(n) // math.factorial(n-r)

# number of Combinations
def nCr(n, r):
    return 0 if r > n else math.factorial(n) // (math.factorial(r)*math.factorial(n-r))

a,b = map(int, input().split())
print(nCr(a, b), '', nPr(a,b))
