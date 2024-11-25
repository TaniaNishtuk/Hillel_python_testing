# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            print("the result is greater than 25, stopping here")
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_of_two_digits(d_first: int | float, d_second: int | float) -> int | float:

    return d_first + d_second


print(f"The sum of two digits: {sum_of_two_digits(789, 456.8)}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def return_some_number(list_of_numbers: list) -> float:

    return sum(list_of_numbers) / len(list_of_numbers)


random_list = [i for i in range(1, 5)]
print(f"Середнє арифметичне: {return_some_number(random_list)}")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reversed_string(user_input: str) -> str:

    return user_input[::-1]


print(f"Обернений рядок: {reversed_string(input('Hey, how was your day?:'))}")
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(list_of_words: list) -> str:
    longest = ""  # пуста змінна для найдовшого слова
    for word in list_of_words:
        if len(word) > len(longest):
            longest = word
    return longest


list_to_search = ['zuika', 'slfkeofjvdkfjfkfmkldfmkdfgjngj', 'candle', 'onion']
print(f"Найдовше слово: {find_longest_word(list_to_search)}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(text, string_to_search):

    return text.find(string_to_search)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 - from homework 5

# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)


def filtering_cars(some_dictionary: dict, search_options: tuple) -> list:
    """
    Function that filters cars by search_options params
    And sorts filtered cars by price and returns first 5 filtered and sorted cars
    :param some_dictionary: dictionary of cars to be filtered and sorted
    :param search_options: tuple of filtering params
    :return: list of filtered and sorted cars
    """
    # фільтрую за роком випуску, о'бємом двигуна та ціною
    filtered_cars = [[name, details] for name, details in some_dictionary.items()
                    if details[1] >= search_options[0]
                    and details[2] >= search_options[1]
                    and details[-1] <= search_options[-1]
                    ]
    # сортую за ціною
    return sorted(filtered_cars, key=lambda car_price: car_price[1][-1], reverse=False)[:5]


print(f" first 5 searched cars :{filtering_cars(car_data, search_criteria)}")


# task 8 - homework 4

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


""" Виведіть, скільки слів у тексті починається з Великої літери?
"""


def find_titled_words(text_to_parse: str) -> int:
    """
    Function that counts quantity of words in string that start with capital letters.
    :param text_to_parse: string value to parse
    :return: int value indicating quantity of titled words
    """

    upper_words = []
    text_to_parse = (text_to_parse
                     .replace("....", " ")
                     .replace("\n", " ")
                     .replace('"', ""))
    text_to_parse = ' '.join(text_to_parse.split()).split(" ")
    for item in text_to_parse:
        if item.istitle():  # тут я перевіряю чи перша буква кожного слова велика
            upper_words.append(item)  # додаю кожне слово в список, якщо воно з великої літери
    return len(upper_words)


print(f"Titled words count: {find_titled_words(adwentures_of_tom_sawer)}")  # 14 words

# task 9 - from homework 6

""""
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""

#  створила окрему функцію щоб отримати інпут від юзера бо використовуватимуїї в двох тасках
#  економлю пайтон чучуть таким чином


def get_input_from_user() -> str:
    """
    Helper function to request input from user
    :return: string value
    """
    input_from_user = (input("Provide any phrase:"))
    return input_from_user


def count_of_unique_symbols(num_of_symbols: int) -> bool:
    """
    Function that checks if there is num_of_symbols in string
    :param num_of_symbols: nt value indicating how many symbols we are searching
    :return: bool value indicating True|False depending on if we have found required quantity of symbols
    """
    # сет компрехеншином вибираю усі унікальні символи
    unique_items = {item for item in get_input_from_user()}
    condition = True  # True by default
    # перевіряю чи є потрібна кількість унікальних символів
    if len(unique_items) > num_of_symbols:
        return condition
    else:
        condition = False
        return condition


num = 10
print(f"Is there required amount of unique symbols: {count_of_unique_symbols(num)}")

# task 10 - from homework 5

"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
(враховуються як великі так і маленькі). Цикл не повинен завершитися,
якщо користувач ввів слово без букви "h".
"""


def find_letter_in_text(symbol_to_search: str) -> bool:
    """
    Function check f specific symbol is present in string
    :param symbol_to_search: symbol to search in string
    :return: True|False depending on if we have found required symbol
    """
    condition = True  # True by default
    while True:
        input_from_user = get_input_from_user()
        if symbol_to_search in input_from_user.lower():
            return condition
        else:
            condition = False
            return condition


symbol = 'h'
print(f"Is required symbol present n text: {find_letter_in_text(symbol)}")
