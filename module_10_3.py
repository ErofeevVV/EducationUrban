import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 500)
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bank = Bank()

deposit_thread = threading.Thread(target=bank.deposit)
take_thread = threading.Thread(target=bank.take)

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f"Итоговый баланс: {bank.balance}")
