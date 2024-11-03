import time
from multiprocessing import Pool


def read_info(file):
    all_data = []
    with open(file, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'Files/file {number}.txt' for number in range(1, 5)]

    # Линейное считывание:
    start_time = time.time()
    for name in filenames:
        read_info(name)
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Время выполнения линейного считывания {total_time:.5f} секунд.')

    # Многопроцессорное считывание:
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Время выполнения многопроцессорного считывания {total_time:.5f} секунд.')
