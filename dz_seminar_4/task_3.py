"""Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""


from decimal import Decimal

MIN_SUM = Decimal(50)
PROCENT_COMMISION = Decimal('0.015')
MIN_COMISSION = Decimal('30')
MAX_COMISSION = Decimal('600')
BONUS = Decimal('0.03')
LIMIT_BEFORE_TAX = Decimal('5000000')
TAX_RATE = Decimal('0.1')


def menu(balance: Decimal, count: int, is_flag: bool, operations: list):
    dct = {'1': 'пополнить счет',
           '2': 'снять со счета',
           '3': 'выйти из программы'}

    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)
    choice = input('Введите команду: ')
    if choice == '3':
        print(balance)
        return balance, is_flag == False
    elif choice == '1':
        balance, operation = give_money(balance)
        operations.append(operation)
        count += 1
    elif choice == '2':
        balance, operation = get_money(balance)
        operations.append(operation)
        count += 1
    else:
        print('Неверная команда')
    if count % 3 == 0:
        balance *= (1 + BONUS)
    print(f'Баланс: {balance}')
    return balance, is_flag


def get_money(balance: Decimal):
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= balance:
            operation = f'Снятие: {money_to_get}, 
                          Комиссия: {procent.normalize().to_eng_string()}'
            return balance - (money_to_get + procent), operation
        else:
            print('Недостаточно средств для снятия')
            return balance, None

    else:
        print('Ошибка, сумма должна быть кратна 50')
        return balance, None


def give_money(balance: Decimal):
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        operation = f'Пополнение: {money_to_give}'
        return balance + money_to_give, operation
    else:
        print('Ошибка, сумма должна быть кратна 50')
        return balance, None


if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат')
    balance = Decimal(0)
    count = 1
    is_flag = True
    operations = []
    while is_flag:
        balance, is_flag = menu(balance, count, is_flag, operations)

    print("Список операций:")
    for op in operations:
        print(op)
