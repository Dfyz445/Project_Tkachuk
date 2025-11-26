#Найти и вывести на экран S=1!+2!+3!+4!+...+n! (n>1).
try:
    n = int(input("Ввести число больше 1: "))
    if n < 1:
        print("Число меньше 1")
except ValueError:
    print("Ошибка")
fact = 1
count = n
count2 = 1
S = 0
while count >= 1:
    fact *= count2
    count -=1
    count2 += 1
    S += fact
print(S)