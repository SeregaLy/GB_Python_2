'''Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.'''

from math import pi

d = 10
l = d * pi
s = pi * (d/2) ** 2
print(f'Диаметр: {d} \nдлина окружности: {l:.42f} \nплощадь круга: {s:.42f}')