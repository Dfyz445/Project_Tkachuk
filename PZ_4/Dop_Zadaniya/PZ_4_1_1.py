"""
Ввести 4 числа.
Найти и вывести на экран сумму и количество отрицательных чисел
"""
try:
    num1, num2, num3, num4 = (float(input("Введите 1 число: ")),
                              float(input("Введите 2 число: ")),
                              float(input("Введите 3 число: ")),
                              float(input("Введите 4 число: ")))
except ValueError:
    print("Введены некорректные числа!")
negative = 0
sum_negative = 0

if num1 < 0:
    negative += 1
    sum_negative += num1
if num2 < 0:
    negative += 1
    sum_negative += num2
if num3 < 0:
    negative += 1
    sum_negative += num3
if num4 < 0:
    negative += 1
    sum_negative += num4

print("Количество отрицательных чисел:", negative)
print("Сумма:", sum_negative)
