#Ввести N чисел. Найти и вывести их среднее арифметическое.
try:
    count_nums = int(input("Введите количество чисел"))
except ValueError:
    print("Введено ни число!")
count1 = count_nums
total = 0
while count1 > 0:
    num1 = float(input("Введите число: "))
    total += num1
    count1 -= 1
average = total / count_nums
print("Среднее арифметическое", average)