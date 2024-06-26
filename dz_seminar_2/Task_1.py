""" 
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата. 

"""


def to_hex(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str


num = int(input("Введите целое число: "))
hex_str = to_hex(num)
print(f"Шестнадцатеричное представление числа {num}: {hex_str}")

# Проверка функцией hex
hex_num = hex(num)
print(f"Шестнадцатеричное представление числа {num}:", hex_num)

