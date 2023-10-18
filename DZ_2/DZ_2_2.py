'''На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь
с числителем и знаменателем. Напишите программу, которая должна возвращать
сумму и произведение дробей. Для проверки своего кода используйте модуль
fractions.'''

import fractions

#frac1 = '1/2'
#frac2 = '1/3'

num1, denom1 = map(int, frac1.split('/'))
num2, denom2 = map(int, frac2.split('/'))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def reduce_fraction(num, denom):  # сокращение дробей
    div = gcd(num, denom)
    return f"{num // div}/{denom // div}"


sum_denom = denom1 * denom2
sum_num = denom2 * num1 + denom1 * num2

prod_num = num1 * num2
prod_denom = denom1 * denom2

print(f'Сумма дробей: {reduce_fraction(sum_num, sum_denom)}')
print(f'Произведение дробей: {reduce_fraction(prod_num, prod_denom)}')

f1 = fractions.Fraction(num1, denom1)
f2 = fractions.Fraction(num2, denom2)

print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')
