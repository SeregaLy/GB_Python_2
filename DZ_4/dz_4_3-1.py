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


def check_multiplicity(amount):
    return amount % MULTIPLICITY == 0


def deposit(amount):
    global bank_account, count, operations

    if not check_multiplicity(amount):
        print(
            f"Сумма должна быть кратной {MULTIPLICITY} у.е. ")
        return

    bank_account += amount
    operations.append(
        f"Пополнение карты на  {amount} у.е. Итого  {bank_account} у.е.")
    count += 1


def withdraw(amount):
    global bank_account, operations

    if not check_multiplicity(amount):
        print(
            f"Сумма должна быть кратной {MULTIPLICITY} у.е. ")
        return

    if amount < MIN_REMOVAL or amount > MAX_REMOVAL:
        print(
            f"Сумма снятия {amount} должна быть между {MIN_REMOVAL} и {MAX_REMOVAL}")
        return

    commission = amount * PERCENT_REMOVAL
    bank_account -= amount + commission
    operations.append(
        f"Снятие суммы {amount}, комиссия составила {commission}")

    print(
        f"Сумма {amount} успешно снята. Комиссия составила {commission}. Текущий баланс: {bank_account}")


def exit():
    global bank_account, operations

    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT
        bank_account -= tax
        operations.append(f"Налог на богатство составил {tax}")


deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
