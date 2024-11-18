"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""
list_of_numbers = list(range(0, 120))  # список чисел від 0 до 119
print(list_of_numbers)
even_nums_sum = sum(num for num in list_of_numbers if num % 2 == 0)  # нагуглила метод sum

print("Сума всіх парних чисел:", even_nums_sum)

# до гуглення мій варіант виглядав отак, але я хотіла зробити через - comprehension

"""
for num in list_of_numbers:
    if num % 2 == 0:  # перевіряю, чи число парне
        even_nums_sum += num 
"""
