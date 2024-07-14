calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    list_lower = []
    for i in list_to_search:
        list_lower.append(i.lower())
    return string.lower() in list_lower


print(string_info('CapiBara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
