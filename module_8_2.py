def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        length = len(numbers) - incorrect_data
        average = result / length
        return (f'Веденных данных: {len(numbers)} из них'
                f'\nчисел: {length}'
                f'\nнекорректных данных: {incorrect_data}'
                f'\nСреднее арифметическое введенных чисел: {round(average, 2)}')
    except TypeError:
        return 'Введен некорректный тип данных!'
    except ZeroDivisionError:
        return 'Нет данных для подсчета среднего арифметического!'


# print(f'Результат 1: {calculate_average("1, 2, 3")}')
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
# print(f'Результат 3: {calculate_average(567)}')
# print(f'Результат 4: {calculate_average([39, 15, 36, 13, 15, 13])}')

