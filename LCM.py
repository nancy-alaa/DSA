import math
def LCM(A, B):
    # GET THE PRIME FACTORS OF EACH OF THEM
    def PrimeFactrors(num):
        sqrt_of_num = math.ceil(math.sqrt(num))
        prime_factors = []
        for i in range(2, sqrt_of_num + 1):
            while num % i == 0:
                num = num // i
                prime_factors.append(i)
        if num != 1:
            prime_factors.append(num)
        return prime_factors
    prime_factors_of_A = PrimeFactrors(A)
    prime_factors_of_B = PrimeFactrors(B)
    print(prime_factors_of_A)
    print(prime_factors_of_B)

    primes_of_A_difference_B = set(prime_factors_of_A).difference(set(prime_factors_of_B))
    primes_of_B_difference_A = set(prime_factors_of_B).difference(set(prime_factors_of_A))

    LCM = 1
    for num in set(prime_factors_of_A):
        if num in set(prime_factors_of_B):
            highest_frequency_of_the_number = max(prime_factors_of_A.count(num), prime_factors_of_B.count(num))
            LCM *= num ** highest_frequency_of_the_number

    if primes_of_A_difference_B:
        for n in set(primes_of_A_difference_B):
            LCM *= n**prime_factors_of_A.count(n)

    if primes_of_B_difference_A:
        for n in set(primes_of_B_difference_A):
            LCM *= n ** prime_factors_of_B.count(n)
    return LCM

print(LCM(3, 8))