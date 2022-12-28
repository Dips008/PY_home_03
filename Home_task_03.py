# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

lst = []
for i in range(5):
    lst.append(random.randint(101, 1000) / 100)
print(lst, ' => ', end = '')


max = 0
min = 1
for e in range(len(lst)):
   if max < (lst[e] % 1):
      max = (lst[e] % 1)
   if min > lst[e] % 1:
      min = lst[e] % 1
      
print(round(max-min, 2))