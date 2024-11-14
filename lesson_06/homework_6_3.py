"""
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими
"""

initial_list = ['', '2', 2, 46, True, 'jungle', 2.7, ['banana', 34], {'a', 3333}, 'catito']
new_only_string_list = [item for item in initial_list if type(item) == str]
print(new_only_string_list)
# ще був такий варіант
# new_only_string_list = [item for item in initial_list if isinstance(item, str)]