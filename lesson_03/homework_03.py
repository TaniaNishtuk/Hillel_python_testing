alice_in_wonderland = (
    " - Would you tell me, please, which way I ought to go from here?\n"
    " - That depends a good deal on where you want to get to, —— said the Cat.\n"
    " - I don\'t much care where, —— said Alice.\n"
    " - Then it doesn\'t matter which way you go, —— said the Cat.\n"
    " - —— so long as I get somewhere, —— Alice added as an explanation.\n"
    " - Oh, you\'re sure to do that, —— said the Cat, —— if you only walk long enough."
)
print(alice_in_wonderland)
# Тут я не впевнена, що правильно зрозуміла другий пункт першого завдання
# Також я трішки змінила розділові знаки, щоб текст був у форматі діалогу


# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
azov_sea_surface_area = 37800
black_sea_surface_area = 436402
commulative_surface_area = azov_sea_surface_area + black_sea_surface_area
print(
    f"Ми знаємо, що площа Чорного моря = {black_sea_surface_area} км2\n"
    f"А площа Азовського моря становить = {black_sea_surface_area} км2\n"
    f"Загальна площа двох морів = {commulative_surface_area} км2"
    )

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

warehouse = 3
total_goods_amount = 375291
first_second_warehouse_goods_amount = 250449
second_third_warehouse_goods_amount = 222950

first_warehouse_goods = total_goods_amount - second_third_warehouse_goods_amount
third_warehouse_goods = total_goods_amount - first_second_warehouse_goods_amount
second_warehouse_goods = total_goods_amount - first_warehouse_goods - third_warehouse_goods

# Виведемо результати
print(f"Кількість товарів на першому складі = {first_warehouse_goods}\n"
      f"Кількість товарів на другому складі = {second_warehouse_goods}\n"
      f"Кількість товарів на третьому складі = {third_warehouse_goods}"
     )

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
price_per_month = 1179
number_of_payments = 18
laptop_price = price_per_month * number_of_payments
print(f"Михайло за батьками купують комп'ютер за допомогою послуги оплата частинами\n"
      f"Салачувати потрібно буде {price_per_month} гривень кодного місяця впродовж {number_of_payments} місяців\n"
      f"Загальна вартість комп'ютера становить = {laptop_price} гривні")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
numbers = [a, b, c, d, e, f]
for num in numbers:
    print(f"Остача від ділення числа = {num}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274
medium_pizza = 218
juice = 35
cake = 350
water = 3
total_products_price = (big_pizza * 4) + (medium_pizza * 2) + (juice * 4) + cake + (water * 3)
print(f"Іринка замовила 4 великі та 2 середні піци за ціною = {big_pizza+medium_pizza} гривні\n"
      f"А також воду, сік та торт за ціною {juice+cake+water} гривні\n"
      f"Загальна сумна замовлення склала = {total_products_price} гривня"
      )

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
max_per_page = 8
min_pages_required = all_photos / max_per_page
print(f"Ігор має {all_photos} фотографії, які він хоче вклеїти в альбом\n"
      f"Максимальна кількість фото, які можна вміститись на сторінку = {all_photos} фотографій\n"
      f"Отож потрібно мінімум {int(min_pages_required)} сторінок у альбомі для усіх фотографій"
      )

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_per_100_km = 9
tank_capacity = 48

total_fuel_needed = (distance / 100) * fuel_per_100_km

km_per_full_tank = (tank_capacity / fuel_per_100_km) * 100
refuel_count_times = distance / km_per_full_tank

print(f"Загальна кількість бензину, необхідного для подорожі = {total_fuel_needed} літрів\n"
      f"Мінімальна кількість заправок, необхідних для подорожі = {int(refuel_count_times)}"
      )
