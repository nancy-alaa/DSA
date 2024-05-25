import math
x, y, z = sorted(list(map(int, input().split())))
if x+y > z:
    print("Valid")
    summ = x + y + z
    print(math.sqrt((summ//2) * (summ//2 - x) * (summ//2 - y) * (summ//2 - z)))
else:
    print("Invalid")