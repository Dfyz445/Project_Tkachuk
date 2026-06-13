#В матрице элементы кратные 3 увеличить в 3 раза.

matrix = [
    [1, 3, 5, 6],
    [9, 2, 4, 12],
    [7, 8, 15, 0]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] *= 3

print("Матрица после увеличения элементов, кратных 3, в 3 раза:")
for row in matrix:
    print(row)