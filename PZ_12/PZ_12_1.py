#В матрице элементы кратные 3 увеличить в 3 раза.
import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = [[random.randint(1, 30) for _ in range(rows)] for _ in range(cols)]

print("Исходная матрица:")
for row in matrix:
    print(row)

processed_matrix = list(map(
    lambda row: list(map(
        lambda x: x * 3 if x % 3 == 0 else x,
        row
    )),
    matrix
))

print("Матрица после увеличения элементов, кратных 3, в 3 раза:")
list(map(lambda row: print(row), processed_matrix))