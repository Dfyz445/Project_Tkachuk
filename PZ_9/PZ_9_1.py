"""
Имеется список студентов группы, в котором все имена различны.
Определить, есть ли в группе студент, который побывал в гостях у всех студентов.
(Для каждого студента составить список из множества побывавших у него в гостях друзей,
причем хозяина в этот список не включать).
"""
students = ["Иван","Артем","Миша","Даня","Гена","Маша","Катя"]
visited ={
    "Иван": {"Даня","Гена","Маша","Катя"},
    "Артем": {"Иван","Даня","Гена","Маша","Катя"},
    "Миша": {"Иван","Артем","Даня","Гена","Маша","Катя"},
    "Даня": {"Иван","Артем","Миша"},
    "Гена": {"Миша","Даня"},
    "Маша": {"Катя"},
    "Катя": {"Иван","Артем","Миша"}
}

students_copy = students
count = 0
cc = 0
while count < 7:
    students = set(students_copy)

    if count == 0:
        students.remove("Иван")
        if students == visited["Иван"]:
            cc += 1
    elif count == 1:
        students.remove("Артем")
        if students == visited["Артем"]:
            cc += 1
    elif count == 2:
        students.remove("Миша")
        if students == visited["Миша"]:
            cc += 1
    elif count == 3:
        students.remove("Даня")
        if students == visited["Даня"]:
            cc += 1
    elif count == 4:
        students.remove("Гена")
        if students == visited["Гена"]:
            cc += 1
    elif count == 5:
        students.remove("Маша")
        if students == visited["Маша"]:
            cc += 1
    elif count == 6:
        students.remove("Катя")
        if students == visited["Катя"]:
            cc += 1
    count += 1


if cc > 0:
    print(f"В группе {cc} студентов были у всех")
else:
    print("В группе нет студентов которые были у всех")