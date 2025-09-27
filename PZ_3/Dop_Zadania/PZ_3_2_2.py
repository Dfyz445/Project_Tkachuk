try:
    num1 = float(input("Введите число:"))
    if num1 % 2 == 0:
        num1 /= 4
    else:
        num1 *= 5
    print(num1)
except ValueError:
    print("Это не число!")