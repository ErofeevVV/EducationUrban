# def min_(lst):
#     return min(lst)
#
# def max_(lst):
#     return max(lst)
#
# def len_(lst):
#     return len(lst)
#
# def sum_(lst):
#     return sum(lst)
#
# def sorted_(lst):
#     return sorted(lst)
#
# def apply_all_func(int_list, *functions):
#     results = {}
#     for func in functions:
#         results[func.__name__] = func(int_list)
#     return results
#
#
# print(apply_all_func([6, 20, 15, 9], max, min))
# print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


"""Функции указанные в задании не имеют смыcла (являются встроенными?),
т.к. функция apply_all_func может работать самостоятельно:"""

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
