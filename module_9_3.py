first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


def line_length_difference(list1, list2):
    differences = []
    for item1, item2 in zip(list1, list2):
        length_diff = abs(len(item1) - len(item2))
        if length_diff > 0:
            differences.append(length_diff)
    return differences


'''def length_check(list1, list2):
    results = []
    for item1, item2 in zip(list1, list2):
        is_equal = len(item1) == len(item2)
        results.append(is_equal)
    return results'''


def length_check(list1, list2):
    results = []
    max_length = max(len(list1), len(list2))
    for i in range(max_length):
        try:
            element1 = list1[i]
            element2 = list2[i]
            if len(element1) == len(element2):
                results.append(True)
            else:
                results.append(False)
        except IndexError:
            results.append(False)
    return results


first_result = line_length_difference(first, second)
second_result = length_check(first, second)

print(first_result)
print(second_result)
