def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_in_list = []
        for j in range(m):
            list_in_list.append(value)
        matrix.append(list_in_list)
    return matrix
result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)

#######################################
# ввод значений
#######################################

n = int(input('Введите количество вложеных списков: '))
m = int(input('Введите количество значений в вложеных списках: '))
value = int(input('Введите значение: '))
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_in_list = []
        for j in range(m):
            list_in_list.append(value)
        matrix.append(list_in_list)
    return matrix
result = get_matrix(n, m, value)
print(result)

######################################
#Развернутая матрица
######################################

n = int(input('Введите количество строк '))
m = int(input('Введите количество столбцов: '))
value = int(input('Введите значение: '))
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_in_list = []
        for j in range(m):
            list_in_list.append(value)
        matrix.append(list_in_list)
    return matrix
result = get_matrix(n, m, value)
for list_in_list in result:
    print(*list_in_list)
