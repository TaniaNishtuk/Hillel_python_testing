# lesson_09/__init__.py
# нагуглила цей спосіб налаштування імпортів, щоб у тестовому файлі імпортувати через from lesson_09 import *
from .homework_9 import find_titled_words, filtering_cars, car_data, search_criteria, find_longest_word

# Controls what gets imported with *
__all__ = ["find_titled_words", "filtering_cars", "car_data", "search_criteria", "find_longest_word"]
