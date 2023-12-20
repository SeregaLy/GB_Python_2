'''
Функция группового переименования файлов

Инструкция по использованию платформы



Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
'''

import os
import re
import glob

def rename_files(desired_name, num_digits, original_extension, new_extension, name_range=None):
    directory = "test_folder/"
    files = glob.glob(directory + f"*.{original_extension}")

    for index, file in enumerate(files):
        file_name = os.path.basename(file)
        name_without_extension = os.path.splitext(file_name)[0]

        if name_range:
            name_without_extension = name_without_extension[name_range[0]:name_range[1]]

        new_name = f"{name_without_extension}_{desired_name}_{str(index+1).zfill(num_digits)}.{new_extension}"
        os.rename(file, os.path.join(directory, new_name))
