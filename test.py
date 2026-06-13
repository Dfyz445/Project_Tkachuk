students = {"Иван","Артем","Миша","Даня","Гена","Маша","Катя"}
visited_i = {"Даня","Гена","Маша","Катя"}
visited_A = {"Иван","Даня","Гена","Маша","Катя"}
visited_M = {"Иван","Артем","Даня","Гена","Маша","Катя"}
visited_D = {"Иван","Артем","Миша"}
visited_G = {"Иван","Миша","Даня"}
visited_MA = {"Иван","Катя"}
visited_K = {"Иван","Артем","Миша"}

result = 0

if ("Миша" in visited_i and "Миша" in visited_A and "Миша" in visited_D and
    "Миша" in visited_G and "Миша" in visited_MA and "Миша" in visited_K):
    result += 1

if ("Иван" in visited_A and "Иван" in visited_M and "Иван" in visited_D and
    "Иван" in visited_G and "Иван" in visited_MA and "Иван" in visited_K):
    result += 1

if ("Артем" in visited_i and "Артем" in visited_M and "Артем" in visited_D and
    "Артем" in visited_G and "Артем" in visited_MA and "Артем" in visited_K):
    result += 1

if ("Даня" in visited_i and "Даня" in visited_A and "Даня" in visited_M and
    "Даня" in visited_G and "Даня" in visited_MA and "Даня" in visited_K):
    result += 1

if ("Гена" in visited_i and "Гена" in visited_A and "Гена" in visited_M and
    "Гена" in visited_D and "Гена" in visited_MA and "Гена" in visited_K):
    result += 1

if ("Маша" in visited_i and "Маша" in visited_A and "Маша" in visited_M and
    "Маша" in visited_D and "Маша" in visited_G and "Маша" in visited_K):
    result += 1

if ("Катя" in visited_i and "Катя" in visited_A and "Катя" in visited_M and
    "Катя" in visited_D and "Катя" in visited_G and "Катя" in visited_MA):
    result += 1

if result > 0:
    print(f"В группе {result} студентов были у всех")
else:
    print("В группе нет студентов которые были у всех")