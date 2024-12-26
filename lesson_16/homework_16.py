"""
Завдання 1
Створіть клас Employee, який має атрибути name та salary.
Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size,
який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""
import pytest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self,  name, salary, department, team_size, programming_language):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

@pytest.mark.parametrize(
    "name, salary, department, team_size, programming_language",
    [
        ("Bob", 100000, "IT", 3, "Python"),
        ("Alice", 120000, "Development", 5, "JavaScript"),
        ("John", 95000, "QA", 4, "Ruby"),
    ],
)
def test_teamlead_inherited_and_own_attributes(name, salary, department, team_size, programming_language):
    # створення інстанса класу з усіма можливими атрибутами
    team_lead = TeamLead(name, salary, department, team_size, programming_language)

    # перевіряю значення атрибутів
    assert team_lead.name == name
    assert team_lead.salary == salary
    assert team_lead.department == department
    assert team_lead.programming_language == programming_language
    assert team_lead.team_size == team_size
