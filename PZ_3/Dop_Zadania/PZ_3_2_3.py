try:
    num1 = int(input("Введите двухзначное число:"))
    if 10 <= num1 <= 99 and num1 % 2 == 0:
        num1 += 2
        print(num1)
    elif 10 <= num1 <= 99 and num1 % 2 == 1:
        num1 -= 2
        print(num1)
    else:
        print("Введенно не двухзначное число")
except ValueError:
    print("Ввели не число")