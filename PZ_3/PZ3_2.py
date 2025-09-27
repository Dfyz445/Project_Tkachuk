#2. Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим).

try:
    num1 = float(input("Введите 1 число: "))
    num2 = float(input("Введите 2 число: "))
    num3 = float(input("Введите 3 число: "))
    if num1 > num2 and num1 > num3:
        print(num1, "Самое большое")
    elif num2 > num1 and num2 > num3:
        print(num2, "Самое большое")
    elif num3 > num1 and num3 > num2:
        print(num3, "Самое большое")
except ValueError:
    print("Введите число!")
