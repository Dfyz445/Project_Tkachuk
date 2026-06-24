#В матрице найти среднее арифметическое элементов последних двух столбцов.
import random
from functools import reduce

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = [[random.randint(1, 30) for _ in range(rows)] for _ in range(cols)]

print("Матрица:")
list(map(print, matrix))

cols = len(matrix[0])
if cols >= 2:
    elements = reduce(
        lambda acc, row: acc + row[cols - 2:],
        matrix,
        []
    )

    total = reduce(lambda acc, x: acc + x, elements, 0)
    average = total / len(elements) if elements else None

    print(f"Среднее арифметическое элементов последних двух столбцов: {average}")
else:
    print("Нет элементов для подсчета")