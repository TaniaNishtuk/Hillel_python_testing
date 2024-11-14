""""
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""

string_to_check = input(f"Введіть якусь фразу: ")
unique_items = {item for item in string_to_check}
print(unique_items)
condition = True  # True by defaul
if len(unique_items) > 10:
    print(f"yey, there is more than 10 unique items in this set: {condition}")
else:
    condition = False
    print(f"nope, there is less than 10 unique items in this set: {condition}")
