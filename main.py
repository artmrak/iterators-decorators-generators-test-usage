import random

def my_generator(item):
    yield item

my_iter = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Используем функцию choice() для выбора случайного элемента из списка my_iter
random_item = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

for el in my_iter:
    if el == random_item:
        # Если элемент равен выбранному случайно числу, выводим его с помощью my_generator()
        print(list(my_generator(el))[0])