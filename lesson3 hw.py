#                                                   ЗАДАЧА 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [2, 3, 5, 9, 3]
# summ = 0
#
# for i in range(len(lst)):
#     if i % 2 != 0:
#         summ += lst[i]
# print(f'Сумма элементов на нечетных позициях = {summ}')
# вариант 2
# from random import randint
# lst = []
# for i in range(randint(4,10)):
# lst.append(randint(1,100))
# print(lst)
# sum = 0
# for i in range(len(lst)):
#     if i%2 == 1:
#         sum += lst[i]
# print(sum)



#                                                   ЗАДАЧА 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# lst = [2, 3, 4, 5, 6]
# ln = len(lst)
# for i in range(ln):
#     if i >= ln/2:
#         break
#     print(lst[i] * lst[-i-1], end=' ')



#                                                   ЗАДАЧА 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = [1.1, 1.2, 3.1, 5, 10.01]
# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(f"Разница между максимальным и минимальным значением дробной части элементов: {max(new_lst) - min(new_lst)}")




#                                                   ЗАДАЧА 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число N: '))
# x = ''
# while n > 0:
#     x = str(n % 2) + x
#     n = n // 2
# print(x)

# вариант 2

# n = int(input('Введите число: '))
# print('{0:b}'.format(n))


#                                                   ЗАДАЧА 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n+1-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums
print(get_fibonacci(n))



