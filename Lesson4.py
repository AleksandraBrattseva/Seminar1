#                                                   ЗАДАЧА 1
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# str = '66 5 13 54 3'
# lst = str.split(sep=' ')
# min = max  = int(lst[0])
# print(lst)
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# for i in range(1, len(lst)):
#     if lst[i] > max:
#         max = lst[i]
#     if lst[i] < min:
#         min = lst[i]
# print(f'Минимальный элемент: {min}, Максимальный элемент: {max}')


#                                                   ЗАДАЧА 2
# Найдите корни квадратного уравнения Ax² + Bx + C = 0

# a = int(input('Введите число А: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))
# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     print(x1, x2)
# elif d == 0:
#     x1 = -b / (2 * a)
#     print(x1)
# else:
#     print('Нет решения')

#                                                   ЗАДАЧА 3
# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
hod = 2  #общий делитель
while True:
    if n1 % hod == 0 and n2 % hod == 0:
        print(hod)
        break
    else:
        hod += 1

if n1 > n2:
    hok = n1
else:
    hok = n2
while True:
    if hok % n1 == 0 and hok % n2 == 0:
        print(hok)
        break
    else:
        hok += 1

