immutable_var = (1, 2, 3, 'red', 'green', True)
print('Immutable tuple:', immutable_var)
#immutable_var[3] = 'black'
#print(immutable_var)
#невозможно поменять изменить элемент кортежа, т.к. кортеж является незменяемым объектом. То есть это список, в котором не возможно заменить элементы.
mutable_list = [4, 5, 6, 'blue', 'orange', False]
print('Mutable list:', mutable_list)
mutable_list[3] = 'white'
mutable_list.append(True)
print('Mutable list:', mutable_list)
