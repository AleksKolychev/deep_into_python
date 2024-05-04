"""2. Напишите функцию группового переименования файлов. Она должна:

a. принимать параметр желаемое конечное имя файлов.
   При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла.
   Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
   Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
   К ним прибавляется желаемое конечное имя, если оно передано.
   Далее счётчик файлов и расширение."""

import os

def group_rename_files(desired_name, num_digits, source_ext, dest_ext, name_range=None):
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(source_ext)]
    counter = 1
    
    for file in files:
        if name_range:
            original_name = file[name_range[0]:name_range[1]]
        else:
            original_name = file
        
        new_name = original_name + desired_name + str(counter).zfill(num_digits) + dest_ext
        os.rename(file, new_name)
        counter += 1

# Пример использования функции
desired_name = "_new"
num_digits = 3
source_ext = ".txt"
dest_ext = ".txt"
name_range = (3, 6)

print(group_rename_files(desired_name, num_digits, source_ext, dest_ext, name_range))
