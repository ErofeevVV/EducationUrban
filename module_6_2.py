from termcolor import colored


class Vehicle:
    __color_variants = ['black', 'white', 'red', 'blue', 'silver']  # Список допустимых цветов

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner  # Владелец
        self.__model = model  # Модель
        self.__engine_power = engine_power  # Мощьность двигателя
        self.__color = color  # Цвет

    def get_model(self):  # Метод возвращает название модели
        return f'Модель: {self.__model}'

    def get_horsepower(self):  # Метод возвращает мощность двигателя
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):  # Метод возвращает цвет автомобиля
        return f'Цвет: {self.__color.title()}'

    def print_info(self):  # Метод выводит информацию об автомобиле (модель, мощность, цвет, владелец)
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner.title()}')

    def set_color(self, new_color: str):  # Метод изменения цвета (из списка)
        if new_color.lower() in (color.lower() for color in self.__color_variants):
            self.__color = new_color
        else:
            print(colored(f'Нельзя сменить цвет на {new_color}', 'red'))


class Sedan(Vehicle):
    __passengers_limit = 5


vehicle1 = Sedan('Fedor', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
