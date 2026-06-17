#В матрице элементы кратные 3 увеличить в 3 раза.
import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = [[random.randint(1, 30) for _ in range(rows)] for _ in range(cols)]

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