"""Напишите функцию для транспонирования матрицы"""


def transpose_matrix(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

def main():
    matrix = []
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    print("Введите элементы матрицы:")
    for _ in range(rows):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    transposed = transpose_matrix(matrix)
    
    print("Исходная матрица:")
    for row in matrix:
        print(row)
    
    print("Транспонированная матрица:")
    for row in transposed:
        print(row)

if __name__ == "__main__":
    main()
    