def minimum(lst):
    return f'Минимальное значение в списке: {min(lst)}.'

def maximum(lst):
    return f'Максимальное значение в списке: {max(lst)}.'

def list_length(lst):
    return f'Длина списка: {len(lst)} символов.'

def list_sum(lst):
    return f'Сумма чисел списка: {sum(lst)}.'

def list_sorted(lst):
    return f'Отсортированный список: {sorted(lst)}.'

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], maximum, minimum))
print(apply_all_func([6, 20, 15, 9], list_length, list_sum, list_sorted))
