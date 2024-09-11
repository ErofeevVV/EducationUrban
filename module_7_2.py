def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(strings, start=1):
            position = f.tell()    # получаем текущую позицию в байтах перед записью
            f.write(string + '\n')  # записываем строку в файл с новой строки
            strings_positions[(index, position)] = string   # заполняем словарь

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
