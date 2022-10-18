# 4.3. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import random

# # решение без анонимных функций
# numbers = []
# for i in range(10):
#     numbers.append(int(random()*10))
# print(numbers)
# result = []
# for k in numbers:
#     if numbers.count(k) == 1: # считаем кол-во элементов i в списке
#         result.append(k)
# print(result)

# # решение через анонимные функции
# numbers = [int(random()*10) for i in range(10)]
# print(numbers)
# result = [k for k in numbers if numbers.count(k) == 1]
# print(result)

# 3.1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# # решение без анонимных функций
# array = [2, 3, 5, 9, 3]
# summ = 0
# for i in range(1, len(array), 2):
#     summ = summ + array[i]
# print(summ)

# решение через анонимные функции
# не получается... пытаюсь, но что-то не то, не понимаю, к чему преоборазовать map, чтобы был ответ, а не тип
# array = [2, 3, 5, 9, 3]
# summ = 0
# print(map((lambda i: summ + array[i], array), (i for i in range(1, len(array), 2))))

# 3.2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# # решение без анонимных функций
# import math
#
# array = [2, 3, 4, 5, 6]
# prod_array = []
# prod = 1
# for i in range(math.ceil(len(array)/2)):
#     prod_array.append(int(array[i] * array[len(array)-i-1]))
# print(prod_array)

# решение через анонимные функции
# import math
#
# array = [2, 3, 4, 5, 6]
# prod = 1
# prod_array = list((int(array[i] * array[len(array)-i-1])) for i in range(math.ceil(len(array)/2)))
# print(prod_array)

# 2.1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

# # решение без анонимных функций
# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

# # решение через анонимные функции
# # не получается вывести ответ вместо типа данных..
numb = float(input())
summ = 0
print(summ + int(el) for el in str(numb) if el != '.')
