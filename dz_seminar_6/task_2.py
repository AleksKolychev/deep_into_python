""" Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i][0] == queens[j][0] or \
                queens[i][1] == queens[j][1] or \
                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

if __name__ == "__main__":
    queens = []
    for _ in range(8):
        x, y = map(int, input().split())
        queens.append((x, y))

    result = check_queens(queens)
    print(result)
    