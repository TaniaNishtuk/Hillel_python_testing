"""
Завдання 2
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Romb:
    def __init__(self, diagonal_1, diagonal_2):
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2

    def calculate_area(self):
        return (self.diagonal_1 * self.diagonal_2) / 2



class Trapezia:
    def __init__(self, a, b, height):
        self.a = a  # довжина першої основи
        self.b = b  # довжина другої основи
        self.height = height  # висота

    def calculate_area(self):
        return ((self.a + self.b) * self.height) / 2



square = Square(10)
print(f"Площа квадрата: {square.calculate_area()}")

circle = Circle(15)
print(f"Площа кола: {circle.calculate_area()}")

romb = Romb(45, 65)
print(f"Площа ромба: {romb.calculate_area()}")

trapezia = Trapezia(10, 6, 4)
print(f"Площа трапеції: {trapezia.calculate_area()}")
