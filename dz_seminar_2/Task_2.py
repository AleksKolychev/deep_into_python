""" 
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions 

"""


from fractions import Fraction

def get_fraction():
    fraction_str = input("Введите дробь в формате a/b: ")
    numerator, denominator = map(int, fraction_str.split('/'))
    return Fraction(numerator, denominator)


fraction1 = get_fraction()
fraction2 = get_fraction()

sum_result = fraction1 + fraction2
product_result = fraction1 * fraction2

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)


# Проверка модулем fractions
f1 = Fraction(2, 5)
print(f1)
f2 = Fraction(4, 5)
print(f2)
print(f1 + f2)
print(f1 * f2)

