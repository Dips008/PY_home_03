# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

lst = []
for i in range(5):
    lst.append(random.randint(1, 10))


res = []
for e in range(int(len(lst) / 2) + 1):
    if e < int(len(lst) / 2):
        res.append(lst[e] * lst[len(lst) - 1 - e])
    elif len(lst) % 2 != 0:
        res.append(lst[e]**2)

print(lst, ' => ', res)
