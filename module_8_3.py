class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        if not isinstance(vin, int):
            raise IncorrectVinNumber(f'Некорректный тип vin номер: {vin}')
        elif vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера: {vin}')

        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров: {numbers}')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(f'Неверная длина номера: {numbers}')


if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
