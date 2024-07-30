class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существвует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


house1 = House('Звездный', 12)
house2 = House('Рождественский', 7)

house1.go_to(7)
house1.go_to(0)
house2.go_to(10)
