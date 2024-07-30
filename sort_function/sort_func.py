# Пузырьковая сортировка:

def bubble_sort(list_):
    for i in range(len(list_) - 1, 0, -1):
        for j in range(i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
    return list_


# Сортировка выбором:

def selection_sort(list_):
    for i in range(len(list_) - 1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[min_index] > list_[j]:
                min_index = j
                list_[min_index], list_[j] = list_[j], list_[min_index]
    return list_


# Сортировка вставками:

def insertion_sort(list_):
    for i in range(1, len(list_)):
        key = list_[i]
        j = i - 1
        while list_[j] > key and j >= 0:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key
    return list_
