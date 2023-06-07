# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits = ['яблоко', 'груша', 'киви', 'апельсин']
right_offset = len(max(fruits, key=len))
for index, item in enumerate(fruits, start = 1):
    print('{}. {:>{}}'.format(index, item, right_offset))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
spisok_1 = ['Sasha', 'Katya', 'Egor', 'Gvidon']
spisok_2 = ['Masha', 'Misha', 'Gvidon']
for y in spisok_2:
    while y in spisok_1:
        spisok_1.remove(y)
print(spisok_1)

