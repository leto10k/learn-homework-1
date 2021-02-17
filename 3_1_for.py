"""

Домашнее задание №1

Цикл for: Цикл

* Создать список из десяти целых чисел.
* Вывести на экран каждое число, увеличенное на 1.

"""

import random
spisok =[]
for i in range(10):
    spisok.append(random.randint(-100,100))
print(spisok)

for i in spisok:
    i += 1
    print(i)    