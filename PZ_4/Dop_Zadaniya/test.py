from random import randint

#Статы
hp_mob1 = 0
hp = 0
mana = 0
exp = 0
lvl_GG = 1

#Выбор класса
print("Добро пожаловать игрок! Выбери класс:")
GG_class = int(input("(Hero, Mag, Archer(1,2,3))"))
if GG_class == 1:
    hp = 200
    mana = 10
    print('Ты выбрал класс "Герой", твои статы(hp, mana):', hp, mana)
elif GG_class == 2:
    hp = 100
    mana = 100
    print('Ты выбрал класс "Маг", твои статы(hp, mana):', hp, mana)
elif GG_class == 3:
    hp = 100
    mana = 50
    print('Ты выбрал класс "Лучник", твои статы(hp, mana):', hp, mana)

#Куда идти
vibor = int(input("Выбери куда тебе пойти(1 - на охоту, 2 - _____, 3 - _______)"))
if vibor == 1:
    fight = randint(1, 100)
    if fight < 50:
        hp_mob1 = 5
        print("Тебе на пути попался кабан")
        vibor_fight = int(input("1 - атаковать, 2 - сбежать "))
        if vibor_fight == 1:
            print("Вы решаетесь атаковать:")
            skill = int(input("Вам доступно: 1 - удар мечом"))
            if skill == 1:
                miss = randint(1, 100)
                if miss < 50:
                    hp_mob1 -= randint(1, 3)
                    print("Удача! -", hp_mob1)
                else:
                    hp -= randint(1, 3)