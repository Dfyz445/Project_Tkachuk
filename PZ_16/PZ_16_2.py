"""
Создание базового класса "Транспортное средство" и его наследование для создания классов "Автомобиль" и "Мотоцикл".
В классе "Транспортное средство" будут общие свойства, такие как максимальная скорость и количество колес,
а классы- наследники будут иметь свои уникальные свойства и методы.
"""
class Vehicle:

    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

    def info(self):
        return f"Скорость: {self.max_speed} км/ч, Колес: {self.wheels}"

class Car(Vehicle):

    def __init__(self, max_speed, color):
        super().__init__(max_speed, wheels=4)
        self.color = color

    def info(self):
        return f"Автомобиль {self.color}, {super().info()}"

    def beep(self):
        return "Бип-бип!"


class Motorcycle(Vehicle):
    def __init__(self, max_speed, has_helmet):
        super().__init__(max_speed, wheels=2)
        self.has_helmet = has_helmet

    def info(self):
        helmet = "есть" if self.has_helmet else "нет"
        return f"Мотоцикл (шлем: {helmet}), {super().info()}"

    def rev(self):
        return "Врум-врум!"

car = Car(200, "красный")
moto = Motorcycle(150, True)

print(car.info())
print(car.beep())

print(moto.info())
print(moto.rev())