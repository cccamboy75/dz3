#Создайте список случайных чисел, со случайным количеством элементов от 3 до 10.
#Ваше задача - создать новый список из 3 элементов начального списка -  первым, третьим и вторым с конца .
#Пример:
#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 1, 1] == [1, 1, 1]
#[6, 3, 7] == [6, 7, 3]

import random
a = []
for i in range(random.randint(3, 10)):
    a.append(random.randint(1, 100))
print(a)
print([a[0]] + [a[2]] + [a[-2]])
