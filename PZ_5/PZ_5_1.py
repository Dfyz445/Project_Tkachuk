"""
Составить программу, в которой функция генерирует четырехзначное число
и определяет, есть ли в числе одинаковые цифры.
"""
import random
#Создаем функцию
def random_number():
    random_num = random.randint(1000, 9999)
    print("Сгенерирированое число:", random_num)

    #Находим каждую цифру в числе
    digit1 = random_num // 1000
    digit2 = (random_num // 100) % 10
    digit3 = (random_num // 10) % 10
    digit4 = random_num % 10

    #Проверяем равны ли они
    if digit1 == digit2 or digit1 == digit3 or digit1 == digit4:
        print("В числе есть одинаковые числа")
    elif digit2 == digit3 or digit2 == digit4:
        print("В числе есть одинаковые числа")
    elif digit3 == digit2 or digit3 == digit4:
        print("В числе есть одинаковые числа")
    else:
        print("В числе нет одинаковых чисел")
    return random_num
#Выполняем вызов функции
print(random_number())