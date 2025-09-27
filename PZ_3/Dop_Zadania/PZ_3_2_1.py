try:
    num1, num2 = float(input("Введите 1 число:")), float(input("Введите 2 число:"))
    num3 = (num1 + num2)
    if num3 < 0:
        num3 *= 8
    else:
        num3 *= 1.5
    print(num3)
except ValueError:
    print("это не число!")