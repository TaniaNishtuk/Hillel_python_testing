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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer_without_n = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer_without_n)
print("-"*200)
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_without_tripple_dots = adwentures_of_tom_sawer_without_n.replace("....", " ")
print(adwentures_of_tom_sawer_without_tripple_dots)
print("-"*200)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
reformatted_text = ' '.join(adwentures_of_tom_sawer_without_tripple_dots.split())
print(f"Текст без зайвих пробілів, '....'  та без '\\n', "
      f"я використовуватиму його у декількох наступних завданнях для зручності:\n{reformatted_text}")
print("-"*200)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

letter_h_count = adwentures_of_tom_sawer.count("h")
print(f"У тексті знайдено {letter_h_count} літер 'h'")  # 40 літер h
print("-"*200)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# у 60 рядку перевиокристовую змінну створену у третьому завданні, щоб не дублювати код - reformatted_text
# таким чином я буду перевіряти вже відформатований текст без зайвих символів
big_letter_counter = 0
upper_words = []
list_of_words = reformatted_text.split(" ")
for item in list_of_words:
    if item[0].isupper():   # тут я перевіряю чи перша буква кожного слова велика
        upper_words.append(item)  # додаю кожне слово в список, якщо воно з великої літери
        big_letter_counter += 1
print(f"У тексті знайдено {big_letter_counter} слів, які починаються з великої літери\n"
      f"Список цих слів: {upper_words}")
print("-"*200)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
word = "Tom"
first_time_occurrence = adwentures_of_tom_sawer.find(word)
second_occurrence = adwentures_of_tom_sawer.find(word, first_time_occurrence + 1)
print(f"Перше входження {word} буде на індексі: {first_time_occurrence}")
print(adwentures_of_tom_sawer[first_time_occurrence])  # перевіряю чи буква під цим індексом Т
print(f"Друге входження {word} буде на індексі: {second_occurrence}")
print(adwentures_of_tom_sawer[second_occurrence])  # перевіряю чи буква під цим індексом Т
print("-"*200)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# у 89 рядку перевиокристовую змінну створену у третьому завданні, щоб не дублювати код - reformatted_text
# таким чином я буду перевіряти вже відформатований текст без зайвих символів
# роздільником беру ". " в кінці кожного речення
# ". " щоб у кінці створеного списку з реченнями не додавався зайвий пустий елемент, як при розділенні по крапці
adwentures_of_tom_sawer_sentences = reformatted_text.split(". ")
print(f"Список усіх речень у тексті:\n{adwentures_of_tom_sawer_sentences}")
print("-"*200)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# беру список речень та виводжу четверте з них по індексу 3, приводжу всі літери до нижнього регістру методом - lower
print(f"Четверте речення: \n{adwentures_of_tom_sawer_sentences[3].lstrip().lower()}")
print("-"*200)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
beginning_to_search = "By the time"
for sen in adwentures_of_tom_sawer_sentences:
    if sen.startswith(beginning_to_search, 0):
        print(f"Речення, яке починається з 'By the time':\n{sen}")
print("-"*200)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

sen_words_count = adwentures_of_tom_sawer_sentences[-1].split()
print(f"Кількість слів в останньому реченні:\n{len(sen_words_count)}")  # 24
