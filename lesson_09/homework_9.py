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


def find_longest_word(list_of_words: list) -> str:
    longest = ""  # пуста змінна для найдовшого слова
    for word in list_of_words:
        if len(word) > len(longest):
            longest = word
    return longest


