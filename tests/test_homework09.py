import pytest
from lesson_09 import *


@pytest.mark.parametrize(
    "input_text, expected_count",
    [
        ("Hello World! This Is A Test.", 6),
        ("hello world! This is a Test.", 2),
        ("this is a test with no titled words.", 0),
        ("Hello, World! Isn't It Great? .... Amazing!", 5),
        ("", 0),
        (".... ... ...", 0),
        ("12098765432456789", 0),

    ],
    ids=[
        "all_titled_words",
        "mixed_case_words",
        "all_small_letters_words",
        "special_characters",
        "empty_string",
        "punctuation_only",
        "digits_string",
    ],
)
def test_find_titled_words(input_text: str, expected_count: int):
    assert find_titled_words(input_text) == expected_count


@pytest.mark.parametrize(
    "cars, filter_criteria, expected_result",
    [
        # словник з машинами та серч критеріями з попередньої домашки(імпортовані)
        (car_data, search_criteria, [['Toyota', ('blue', 2021, 1.6, 'hatchback', 25000)],
                                     ['Kia', ('white', 2020, 2.0, 'sedan', 28000)],
                                     ['Hyundai', ('gray', 2019, 1.6, 'suv', 32000)],
                                     ['Mazda', ('red', 2019, 2.5, 'sedan', 32000)],
                                     ['Nissan', ('pink', 2018, 1.8, 'sedan', 35000)]]),
        (car_data, (2017, 1.6, 0), []),
        (car_data, (3000, 1.6, 40000), []),
        (car_data, (2017, 10.09, 40000), []),

    ],
    ids=[
        "filter_by_price_age_and_engine_capacity",
        "no_cars_found_for_zero_price",
        "no_cars_found_for_3000_year",
        "no_cars_found_for_10.09_engine_capacity",
    ]
)
def test_filtering_cars(cars: dict, filter_criteria: tuple, expected_result: list):

    result = filtering_cars(car_data, filter_criteria)
    assert result == expected_result


@pytest.mark.parametrize(
    "words_list, expected_value",
    [
        (["kkfkkfkfk"], "kkfkkfkfk"),
        (['zuika', 'slfkeofjvdkfjfkfmkldfmkdfgjngj', 'candle', 'onion'], "slfkeofjvdkfjfkfmkldfmkdfgjngj"),
        (["",""], ""),
        ([], "")

    ],
    ids=[
        "one_word_list",
        "multiple_words_list",
        "list_with_empty_words",
        "empty_list"
],
)
def test_find_longest_word(words_list: list, expected_value: str):

    actual_word = find_longest_word(words_list)
    assert expected_value == actual_word
