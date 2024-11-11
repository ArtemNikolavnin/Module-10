import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0
        self.lock = threading.Lock()  # Lock для контроля над доступом к ресурсам

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # Задержка на 1 секунду (1 день)
            self.days += 1

            # Блокируем доступ к переменной enemies
            with self.lock:
                self.enemies -= self.power
                if self.enemies < 0:
                    self.enemies = 0

                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")