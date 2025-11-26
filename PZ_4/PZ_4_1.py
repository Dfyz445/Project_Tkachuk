"""
ВАРИАНТ: 18
Дано вещественное число X и целое число N (> 0).
Найти значение выражения 1+ Х + X2/(2!) + ... + XN/(N!) (N! = 12 ...N).
Полученное число является приближенным значением функции ехр в точке Х.
"""
try:
    #Вводим переменные N и X
    N = int(input("Введите целое число больше нуля:"))
    X = float(input("Введите вещественное число:"))
    #Проверяем положительно ли N
    if N <= 0:
        print(N, "число не положительное, или равно 0!")
except ValueError:
    print("Введены некорректные числа!")
#Вводим переменные
num1 = 1 + X
result = 0
fact_count = 1
fact_num = 1
fact_New = 1
degree = 0

while N > 0:
    fact_count = fact_num
    degree += fact_num
    fact_num += 1
    while fact_count > 0: #нахождение факториала
        fact_New *= fact_count
        fact_count -= 1
    result = num1 + X ** degree / fact_New #находим значение выражения
    #Сбрасывание значений
    degree = 0
    fact_New = 1
    N -= 1
print(result)