'''Напишите функцию get_file_info, которая принимает на вход строку - путь к файлу. Функция должна возвращать словарь с информацией о файле:
абсолютный путь до файла.Функция возвращает кортеж из трёх элементов: путь,
имя файла, расширение файла.'''

file_path = "C:/Users/User/Documents/example.txt"


import os


def get_file_info(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    path = os.path.dirname(file_path)
    if not path.endswith('/'):
        path += '/'  # Добавляем символ '/' в конец пути
    name = os.path.basename(file_name)

    return (path, name, file_extension)


print(get_file_info(file_path="C:/Users/User/Documents/example.txt"))
