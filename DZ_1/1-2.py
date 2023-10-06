# Hапишите код, который анализирует число num и сообщает является ли оно
# простым или составным.Используйте правило для проверки: “Число является
# простым, если делится нацело только на единицу и на себя”.Сделайте
# ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Enter a number: "))


# Введите ваше решение ниже
# num = 1


def is_prime(number):
    # Проверяем ограничения на ввод
    if num < 2 or number > 100000:
        return "Число должно быть больше 1 и меньше 100000"

    # Проверяем остальные числа
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} является составным числом"

    return f"{number} является простым числом"


print(is_prime(num))