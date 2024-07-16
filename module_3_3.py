def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, False, 'python']
values_dict = {'a': 10,
               'b': 'слово',
               'c': [15, 20, 25]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['alpha', 30]

print_params(*values_list_2, None)
