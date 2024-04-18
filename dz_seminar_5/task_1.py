"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


import os


def split_path(file_path):
    path, file = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file)
    return path, file_name, file_extension


file_path = "/home/user/documents/example.txt"
result = split_path(file_path)
print(result)
