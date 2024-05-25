import math
def PrimeFactrors(num):
    sqrt_of_num = math.ceil(math.sqrt(num))
    prime_factors = []
    for i in range(2, sqrt_of_num+1):
        while num % i == 0:
            num = num // i
            prime_factors.append(i)
    if num != 1:
        prime_factors.append(num)
    return prime_factors

n = int(input())
print(PrimeFactrors(n))
print("YES") if len(PrimeFactrors(n)) == 1 else print("NO")




