class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):  # оператор равенства
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # оператор меньше
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):  # оператор больше
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __le__(self, other):  # оператор меньше или равно
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):  # оператор больше или равно
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # оператор не равно
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):  # оператор сложения
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self + value
        return self

    def __iadd__(self, value):
        self + value
        return self

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существвует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


house1 = House('Звездный', 12)
house2 = House('Рождественский', 7)

print(house1)
print(house2)

print(house1 == house2)

house2 = house2 + 5
print(house2)
print(house1 == house2)

house1 += 10
print(house1)

house2 = 10 + house2
print(house2)

print(house1 > house1)
print(house1 >= house2)
print(house1 < house2)
print(house1 <= house2)
print(house1 != house2)
