"""
Создайте класс «Круг», который имеет атрибут радиуса и методы для
вычисления площади, длины окружности и диаметра.
"""
import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


# Пример использования
circle = Circle(5)
print(f"Радиус: {circle.radius}")
print(f"Диаметр: {circle.get_diameter():.2f}")
print(f"Длина окружности: {circle.get_circumference():.2f}")
print(f"Площадь: {circle.get_area():.2f}")