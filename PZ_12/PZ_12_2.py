#В матрице найти среднее арифметическое элементов последних двух столбцов.
import random

matrix = [[random.randint(1, 30) for _ in range(3)] for _ in range(3)]

print("Матрица:")
for row in matrix:
    print(row)

rows = len(matrix)
cols = len(matrix[0])


if cols >= 2:
    start_col = cols - 2
else:
    start_col = 0

total_sum = 0
count = 0

for i in range(rows):
    for j in range(start_col, cols):
        total_sum += matrix[i][j]
        count += 1

if count > 0:
    average = total_sum / count
    print(f"Среднее арифметическое элементов последних двух столбцов: {average}")
else:
    print("Нет элементов для подсчета")