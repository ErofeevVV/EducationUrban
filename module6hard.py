import math

class Figure:   # базовый класс
    sides_count = 0

    def __init__(self, *sides):
        self.__sides = list(sides)  # инкапсулированный атрибут списка сторон
        self.__color = []   # инкапсулированный атрибут списка цветов (формат RGB)
        self.filled = False    # публичный атрибут определяющий закрашенность

        if not self.__is_valid_sides(*sides):   # проверка корректности переданный сторон
            raise ValueError("Стороны указаны неверно")

    @staticmethod
    def __is_valid_color(r, g, b):    # метод проверки корректности передачи цвета
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):   # метод изменения цвета с предварительной его проверкой
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):    # метод возвращающий значений цвета
        return self.__color

    def __is_valid_sides(self, *new_sides):    # метод проверки корректности значения сторон
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):    # метод возвращающий значение сторон
        return self.__sides

    def __len__(self):  # метод возвращающий периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):    # метод принимающий новые стороны и изменяющий их
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):   # дочерний класс
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(circumference)    # функция для доступа к методам родительского класса
        self.set_color(*color)    # установка цвета круга
        self.__radius = circumference / (2 * math.pi)   # вычисление радиуса окружности

    def get_square(self):   # метод возвращающий площадь круга
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(a, b, c)
        self.set_color(*color)

    def get_square(self):
        s = self.__len__() / 2  # Полу-периметр
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Формула Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(*([side_length] * 12))  # передаем одну сторону 12 раз
        self.__sides = [side_length] * 12  # переопределяем стороны куба
        self.set_color(*color)

    def get_volume(self):
        return self.__sides[0] ** 3  # объем куба


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)   # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)    # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)    # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)   # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
