# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

lst = []
for i in range(5):
    lst.append(random.randint(1, 10))
print(lst, ' -> In odd positions , the elements ', end='')

sum = 0
for e in range(len(lst)):
    if e % 2 != 0:
        sum += lst[e]
        print(lst[e], ' ', end='')
print(', answer: ', sum)
