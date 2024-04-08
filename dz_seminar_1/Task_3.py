""" 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

print("Программа загадала число от 0 до 1000. У вас есть 10 попыток.")

for i in range(attempts):
    guess = int(input("Введите число: "))
    
    if guess == num:
        print("Поздравляем! Вы угадали число.")
        break
    elif guess < num:
        print("Больше")
    else:
        print("Меньше")
else:
    print(f"Попытки закончились! Загаданное число было {num}.")

