class Horse:
    def __init__(self):
        self.x_distance = 0     # пройденный путь для Лошади
        self.sound = 'Frrr'     # звук, который издает Лошадь

    def run(self, dx):      # метод изменения дистанции
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0     # пройденный путь для Орла
        self.sound = 'I train, eat, sleep and repeat'   # звук, который издает Орел

    def fly(self, dy):      # метод изменения дистанции
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):     # Инициализация родительских классов
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):     # вызов методов из классов-родителей
        super().run(dx)
        super().fly(dy)

    def get_pos(self):      # текущее положение
        return self.x_distance, self.y_distance

    def voice(self):    # звук, унаследованный от классов-родителей(в соответствии с цепочкой наследования)
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
"""print(Pegasus.mro())"""

p1.voice()
