"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:
Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""

class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба має бути більше 0")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути від 0 до 180 градусів")
            super().__setattr__(name, value)
            super().__setattr__("angle_b", 180 - value)  # Автоматично встановлюємо суміжний кут

        elif name == "angle_b":
            raise AttributeError("Значення кут_б задається автоматично на основі кут_а.")

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return (
            f"Romb(side_a={self.side_a}, "
            f"angle_a={self.angle_a}, "
            f"angle_b={self.angle_b})"
        )


romb = Romb(10, 60)
print(romb)  # Rhombus(side_a=10, angle_a=60, angle_b=120)

romb.side_a = 15
print(romb)

romb.angle_a = 160
print(romb)

#romb.angle_b = 90  # Помилка, кут_б не можна встановити
print(romb)

