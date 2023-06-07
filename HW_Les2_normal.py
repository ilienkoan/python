# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print('Задача №1:')

spisok_x = [5, 8, 10, 9, 36, 74, 86, 49]
spisok_y = []
for x in spisok_x:
    y = x ** (0.5)
    if y == int(y):
        spisok_y.append(int(y))
print(spisok_y)

print('Задача №2:')
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# # Склонением пренебречь (2000 года, 2010 года)
days = ['', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
    'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
       'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
       'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
       'тридцатое', 'тридцать первое']
months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
data = '02.11.2013'
day, month, year = data.split('.')
day = int(day)
month = int(month)
year = int(year)
print(days[day], months[month], year, 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print('Задача №3:')

import random

n = int(input('Введите количество рандомных цифр:  '))
spisok_n = []
down_diapazon = -100
up_diapazon = 100
for i in range(n):
    if -100 <= n <= 100:
        spisok_n.append(random.randint(down_diapazon, up_diapazon))
print(spisok_n)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print('Задача №4:')

list_1 = [1, 4, 8, 6, 7, 4, 9, 8]
list_2 = []
list_3 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)
for i in list_1:
    if i in list_1:
        list_3.append(i)
for i in list_2:
    if i in list_3:
        list_3.remove(i)
for i in list_3:
    if i in list_2:
        list_2.remove(i)
print(list_2)

