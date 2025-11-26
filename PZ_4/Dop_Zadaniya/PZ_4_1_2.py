#Ввести 4 числа. Найти и вывести на экран количество четных чисел.

try:
    num1, num2, num3, num4 = (float(input("Введите 1 число: ")),
                              float(input("Введите 2 число: ")),
                              float(input("Введите 3 число: ")),
                              float(input("Введите 4 число: ")))
except ValueError:
    print("Введены некорректные числа!")
even = 0

if num1 % 2 == 0 :
    even += 1
if num2 % 2 == 0:
    even += 1
if num3 % 2 == 0:
    even  += 1
if num4 % 2 == 0:
    even += 1

print("Количество четных чисел:", even)