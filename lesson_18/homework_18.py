"""
Генератори:
Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
Ітератори:
Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
Декоратори:
Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""

def even_numbers(number):
    for number in range(0, number + 1):
        if number % 2 == 0:
            yield number

some_number = 10
for even in even_numbers(some_number):
    print(even)


def fibonacci(numb):
    a, b = 0, 1
    while a <= numb:
        yield a
        a, b = b, a + b

n = 100
for num in fibonacci(n):
    print(num)


class MyReversedList:
    def __init__(self, some_lis):
        self.some_lis = some_lis
        self.index = len(some_lis)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.some_lis[self.index]

some_list = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
my_iterator = MyReversedList(some_list)
for element in my_iterator:
    print(element)


class EvenNumbers:
    def __init__(self, num):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.num:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

n = 21
for even_number in EvenNumbers(n):
    print(even_number)


def my_logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з аргументами: {args} та {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат виконання функції: {result}")
        return result
    return wrapper


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in function '{func.__name__}': {e}")
    return wrapper

@exception_handler
@my_logging_decorator
def simple_func_for_decorators_check(num_1: int, num_2:int):
    result  = num_1 / num_2
    return result

print(simple_func_for_decorators_check(6,5,))
print(simple_func_for_decorators_check(6,0,))