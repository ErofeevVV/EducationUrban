number = input('Введите число: ')


def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    return int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(number)
print(f'Произведение цифр этого числа: {result}')
