# First Line
x1, y1, x2, y2 = map(int, input().split())

# Second Line
x3, y3, x4, y4 = map(int, input().split())

# Two Lines are parallel if and only if their slopes are equal
print("YES") if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1) else print("NO")
