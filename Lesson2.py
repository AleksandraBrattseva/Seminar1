#                                              Задача 1
# Напишите программу, которая выводит нечетные числа из заданного списка и останавливается, если встречает число 554.

import random

# lst = [2, 67, 789, 554, 34, 57]
# lst = [554]
#
# for i in range(random.randint(5, 10)):           # сколько чисел в списке
#     x = random.randint(500, 600)                 # числа от и до
#     lst.append(x)                                # добавляем в список
# random.shuffle(lst)
# print(lst)
#
# for i in lst:
#     if i % 2 != 0:
#         print(i, end=' ')
#     if i == 554:
#         break

#                                              Задача 2
# Сложить числа вещественного числа


# number = '5.679'
# summ = 0
# for i in number:
#     if i != '.':
#         summ += int(i)
# print(summ)

#                                              Задача 3
# Посчитайте, сколько раз символ встречается в строке

s = 'Посчитайте, сколько раз символ встречается в строке'
simvol = 'с'
count = 0
for i in s:
    if i == simvol:
        count += 1
print(count)


