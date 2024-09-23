first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
dict_first_strings = {x: len(x) for x in first_strings if len(x) % 2 == 0}
dict_second_strings = {y: len(y) for y in second_strings if len(y) % 2 == 0}
third_result = {**dict_first_strings, **dict_second_strings}

print(first_result)
print(second_result)
print(third_result)
