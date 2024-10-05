from random import choice

# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))


# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as f:
            for item in data_set:
                if isinstance(item, str):
                    f.write(item + '\n')
                else:
                    f.write(str(item) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:

class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return choice(self.words)


prediction = MysticBall(['Да', 'Нет', 'Наверное'])

print(prediction())
print(prediction())
print(prediction())
