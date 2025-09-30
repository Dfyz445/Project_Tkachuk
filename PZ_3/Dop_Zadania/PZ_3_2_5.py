try:
    num1, num2 = float(input("Введите 1 число:")), float(input("Введите 2 число:"))
    sum = num1 + num2
    if sum % 5 == 0:
        sum += 1
    else:
        sum -= 2
    print(sum)
except ValueError:
    print("Введено не число!")