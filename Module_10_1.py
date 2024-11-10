import threading
from time import sleep, time

# Функция для записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Задержка на 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time()
print(f"Время выполнения функций: {end_time - start_time:.6f} секунд")

# Создание потоков для записи
threads = []
start_time_threads = time()

# Создание и запуск потоков с аргументами
for args in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    t = threading.Thread(target=write_words, args=args)
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

# Взятие текущего времени
end_time_threads = time()
print(f"Время выполнения потоков: {end_time_threads - start_time_threads:.6f} секунд")