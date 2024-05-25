num = int(input())
if num == 1: print(1)
elif num == 2:
    print(1)
    print(1, 1)
else:
    pascal_triangle = [[1], [1, 1]]
    for i in range(2, num):
        temp = [1]
        for j in range(len(pascal_triangle[i - 1]) - 1):
            temp.append(pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j + 1])
        temp.append(1)
        pascal_triangle.append(temp)

    for row in pascal_triangle:
        for n in row: print(n, '', end='')
        print()



