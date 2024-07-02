my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_index = 0
while number_index < len(my_list):
    if my_list[number_index] > 0:
        print(my_list[number_index])
        number_index += 1
    elif my_list[number_index] == 0:
        number_index += 1
    else:
        break

