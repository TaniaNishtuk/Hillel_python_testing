"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
(враховуються як великі так і маленькі). Цикл не повинен завершитися,
якщо користувач ввів слово без букви "h".
"""

while True:
    input_from_user = input("Введіть слово, яке містить хоча б одну букву 'h' або 'H': ")
    if 'h' in input_from_user.lower():
        print("Дякую, ви ввели правильне слово.")
        break  # завершиться, якщо отримав букву 'h'
    else:
        print("Слово не містить букви 'h'.")
