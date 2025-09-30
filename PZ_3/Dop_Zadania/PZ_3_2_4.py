try:
    num1 = int(input("Введите целое число:"))
    if num1 > 0:
        num1 += 20
    else:
        num1 -= 5
    print(num1)
except ValueError:
    print("Введено не число!")