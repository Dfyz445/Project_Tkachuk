"""
Даны три числа.
Найти среднее из них
(то есть число, расположенное между наименьшим и наибольшим).
"""
try:
    #Вводи 3 числа и сверяем их
    num1, num2, num3 = input("Введите 1 число:"), input("Введите 2 число:"), input("Введите 3 число:")
    if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
        print(num1, "Число среднее")
    elif num2 > num3 and num2 < num1 or num2 < num3 and num2 > num1:
        print(num2, "Число среднее")
    elif num3 > num1 and num3 < num2 or num3 < num1 and num3 > num2:
        print(num3, "Число среднее")
    else:
        print("Непредвиденная ошибка, либо 2 и более числа равны")
except ValueError:
    print("Введите число!")
