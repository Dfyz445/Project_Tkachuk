#
try:
    count_nums = int(input("Введите количество чисел"))
except ValueError:
    print("Введено ни число!")
count1 = count_nums
total = 0
zero_nums = 0
while count1 > 0:
    num1 = float(input("Введите число: "))
    total += num1
    count1 -= 1
    if num1 == 0:
        zero_nums += 1
print("Количество чисел равное 0:", zero_nums)