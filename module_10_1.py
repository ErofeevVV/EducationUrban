import threading
import time
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            line = f'Какое-то слово № {i}\n'
            f.write(line)
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start_time_1 = time.time()

print('Последовательный запуск:')
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_1 = time.time()
total_time_1 = end_time_1 - start_time_1
print(f'Работа потоков {total_time_1:.2f} секунд.')

print('Параллельный запуск:')

start_time_2 = time.time()

threads = []
for count, filename in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()
for t in threads:
    t.join()

end_time_2 = time.time()
total_time_2 = end_time_2 - start_time_2
print(f'Работа потоков {total_time_2:.2f} секунд.')
