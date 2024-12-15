"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""


class Student:
    def __init__(self, name: str, last_name: str, average_score: float, age: int):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def update_average_score(self, new_score: float):
        """Метод для зміни середнього балу студента"""
        self.average_score = new_score
        return f"Updated average score of the student is: \n{self.average_score}"


# створення інстанс студента
student = Student(name="Tania", last_name="Nishtuk", age=30, average_score=89.5)
print(f"Average score of the student is: \n{student.average_score}")

# зміна середнього балу студента
updated_score = student.update_average_score(95.0)
print(updated_score)
