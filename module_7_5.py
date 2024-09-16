import os
import time

directory = '.'

# используем os.walk для обхода каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # получаем размер файла
        filesize = os.path.getsize(filepath)

        # получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # выводим информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
