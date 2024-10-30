import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.number_of_enemies = 100
        self.days_of_battle = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.number_of_enemies > 0:
            self.days_of_battle += 1
            self.number_of_enemies -= self.power
            if self.number_of_enemies <= 0:
                break
            print(f'{self.name} сражается {self.days_of_battle} день(дня)..., '
                  f'осталось {self.number_of_enemies} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.days_of_battle} дней(дня)!')


knight_1 = Knight('Artur', 10)
knight_2 = Knight('Richard', 25)

knight_1.start()
knight_2.start()

knight_1.join()
knight_2.join()

print('Все битвы закончились!')
