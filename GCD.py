# Euclidean Algorithm
# GCD(A, B) = GCD(B, A%B)
# while B != 0 ----- TIME COMPLEXITY = O(log(max(A, B)))
def GCD(A, B):
    while B != 0:
        temp = A
        A = B
        B = temp % B
    return A
print((GCD(24, 6)))