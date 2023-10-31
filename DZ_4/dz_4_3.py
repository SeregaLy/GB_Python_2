'''У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и
проведенных операциях.
Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную
сумму. Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма
снятия также должна быть кратной MULTIPLICITY. При снятии средств начисляется
комиссия в процентах от снимаемой суммы, которая может варьироваться от
MIN_REMOVAL до MAX_REMOVAL.
Завершение работы:
Функция exit() завершает работу с банковским счетом. Перед завершением, если
на счету больше RICHNESS_SUM, начисляется налог на богатство в размере
RICHNESS_PERCENT процентов.
Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному
множителю MULTIPLICITY. Реализуйте программу для управления банковским счетом,
используя библиотеку decimal для точных вычислений.'''

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(
        amount):  # Проверка кратности суммы при пополнении и снятии.
    global bank_account
    if amount % MULTIPLICITY == decimal.Decimal(0):
        bank_account += amount
        return True
    else:
        return False


def deposit(amount):  # Пополнение счета.
    global bank_account
    if check_multiplicity(
            amount):  # Проверка кратности суммы при пополнении и снятии.
        bank_account += amount
        return True
    else:
        return False


def withdraw(
        amount):  # Снятие средств. Сумма снятия также должна быть кратна MULTIPLICITY.
    global bank_account
    if check_multiplicity(
            amount):  # Проверка кратности суммы при пополнении и снятии.
        if amount >= MIN_REMOVAL and amount <= MAX_REMOVAL:
            bank_account -= amount
            return True
        else:
            return False
    else:
        return False


def exit():  # Завершение работы и вывод итоговой информации о состоянии счета и
    # проведенных операциях.
    global bank_account
    global count
    global operations
    if bank_account >= RICHNESS_SUM:
        bank_account += bank_account * RICHNESS_PERCENT
        count += 1
        operations.append(f'Пополнение счета: {bank_account}')
        operations.append(
            f'Комиссия: {bank_account * PERCENT_DEPOSIT}')  # Комиссия в процентах от снимаемой суммы.
    print(
        f'Итоговый баланс: {bank_account}')  # Итоговый баланс. Если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.


deposit(10000)
withdraw(4000)
exit()

print(operations)