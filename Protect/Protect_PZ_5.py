def negative_num():
    num1 = 2
    while num1 < N:
        if num1 % 2:
            print(num1)
            num1 += 1
        else:
            num1 += 1
    return num1

N = int(input("Введите число:"))
print(negative_num())