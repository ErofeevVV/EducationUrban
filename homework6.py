#Словарь

my_dict = {'Pink': [255, 192, 203],
           'SeaGreen': [46, 139, 87],
           'Violet': [238, 130, 238]}
print(my_dict)
print(my_dict['Pink'])
print(my_dict.get('Green', 'Такого цвета нет'))
my_dict.update({'Brown': [165, 42, 42],
                'SkyBlue': [135, 206, 235]})
color = my_dict.pop('Violet')
print(color)
print(my_dict)

#Множества

my_set = {152, 153, 154, 152, 154, True, False, True, 'Green', 'Pink', 'Orange', 'Pink'}
print(my_set)
my_set.add('Black')
my_set.add(158)
my_set.discard(152)
print(my_set)
