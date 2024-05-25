rows1, cols1 = map(int, input().split())
matrix1 = []
for _ in range(rows1):
    matrix1.append(list(map(int, input().split())))

matrix2 = []
rows2, cols2 = map(int, input().split())
for _ in range(rows2):
    matrix2.append(list(map(int, input().split())))

matrix2_rotation = []
for i in range(cols2):
    row = []
    for j in range(rows2):
        row.append(matrix2[j][i])
    matrix2_rotation.append(row)

output = []

for row in matrix1:
    temp = []
    for row1 in matrix2_rotation:
        temp.append(sum([a*b for a, b in zip(row, row1)]))
    output.append(temp)

for row in output:
    for num in row: print(num, '', end='')
    print()
