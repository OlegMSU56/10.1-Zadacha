import time
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(100, 'example3.txt')

end_time = time.time()
print(f'Время выполнения последовательного вызова: {end_time - start_time} секунд')

first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30, 'example6.txt'))
third = Thread(target=write_words, args=(100, 'example7.txt'))

start_time = time.time()

first.start()
second.start()
third.start()

first.join()
second.join()
third.join()

end_time = time.time()
print(f'Время выполнения параллельного вызова: {end_time - start_time} секунд')
