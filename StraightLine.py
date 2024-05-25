x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

#if two lines have the same slope pass through a common point, then the two lines will coincide. In other words, if A, B, and C are three points in the XY-plane, they will lie on a line, i.e., three points are collinear if and only if the slope of AB is equal to the slope of BC.
print("YES") if (y3-y2)*(x2-x1) == (y2-y1)*(x3-x2) else print("NO")
