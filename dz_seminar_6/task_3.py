"""Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""

import random

def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def random_queens_placement():
    queens = []
    for _ in range(8):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        queens.append((x, y))
    return queens

if __name__ == "__main__":
    successful_placements = 0
    while successful_placements < 4:
        queens = random_queens_placement()
        result = check_queens(queens)
        if result:
            print(f"Successful placement: {queens}")
            successful_placements += 1
