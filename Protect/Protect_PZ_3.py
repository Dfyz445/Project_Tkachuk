num1 = float(input("Введите 1 число"))
num2 = float(input("Введите 2 число"))
sum1 = num1 + num2
if 100 <= sum1 <= 200:
    print(sum1, "Лежит на промежутке")
else:
    print(sum1, "Не лежит на промежутке")