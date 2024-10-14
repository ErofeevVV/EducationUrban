def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1 and all(result % i != 0 for i in range(2, result)):
            print('Сумма чисел является простым числом')
        else:
            print('Сумма чисел является составным числом')
        return result
    return wrapper

@is_prime
def sum_numbers(*args):
    res = 0
    for i in args:
        try:
            if isinstance(i, int):
                res += int(i)
        except ValueError:
            print('Введеное значение не является числом!')
            return None
    return res


numbers = input('Введите числа через запятую: ')


try:
    numbers = [int(i) for i in numbers.split(',')]
    result = sum_numbers(*numbers)
    if result is not None:
        print(f'Сумма введенных чисел равна: {result}')
except ValueError:
    print('Введенные значения должны быть числами!')
except NameError:
    print('Введенные значения должны быть числами!')
