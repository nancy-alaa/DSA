import math
def CountMaxDistinctNumbers(num):
    return int((-1 + math.sqrt(1 + 8 * num)) // 2)
print(CountMaxDistinctNumbers(int(input())))