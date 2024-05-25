import math
# x, y is the center of the circle
x, y, r, n = map(int, input().split())
for _ in range(n):
    x2, y2 = map(int, input().split())
    print("YES") if (math.sqrt((pow(x-x2, 2) + (pow(y-y2, 2)))) <= r) else print("NO")

