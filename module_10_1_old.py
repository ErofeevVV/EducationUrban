import threading
from time import sleep


def numbers():
    for i in range(1, 11):
        print(i)
        sleep(1)


def letters():
    for i in 'abcdefghij':
        print(i)
        sleep(1)


numbers_thread = threading.Thread(target=numbers)
letters_thread = threading.Thread(target=letters)

numbers_thread.start()
letters_thread.start()

numbers_thread.join()
letters_thread.join()
