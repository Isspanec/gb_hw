﻿__author__ = 'Анциферов Дмитрий Александрович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
i = 0
a = input('Введите число: ')
a = str(a)
while i < len(a):
 print(a[i])
 i += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = int(input("Введите перове число А "))
b = int(input("Введите второе число B "))
c = a
a = b
b = c

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
if int(input("введите свой возраст ")) => 18:
   print("Доступ разрешен")
else:
   print("Извините, пользование данным ресурсом только с 18 лет")