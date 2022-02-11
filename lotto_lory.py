from functools import cache
import multiprocessing
import random
from tkinter import N
from tkinter.messagebox import NO


print('--- 5-ös lottó számok sorsolása ---')


class Lotto:


    def __init__(self):
        self.win = int(input('Win: '))
        self.total = 0
        self.sajat_szamok = []
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        


    def take_input(self):
        for i in range(5):
            self.sajat_szamok.append(int(input(f'Add meg a(z) {i+1}. számot: ')))


    @cache
    def core_1(self):
        while True:
            random_szamok = [random.randint(1, 99) for _ in range(5)]

            counter = 0
            for data in self.sajat_szamok:
                if data in random_szamok:
                    counter += 1
                    self.total += 1

            if counter == self.win:
                print(f'Total c1: {self.total}')



    @cache
    def core_2(self):
        while True:
            random_szamok = [random.randint(1, 99) for _ in range(5)]

            counter = 0
            for data in self.sajat_szamok:
                if data in random_szamok:
                    counter += 1
                    self.total += 1

            if counter == self.win:
                print(f'Total c2: {self.total}')



    @cache
    def core_3(self):
        while True:
            random_szamok = [random.randint(1, 99) for _ in range(5)]

            counter = 0
            for data in self.sajat_szamok:
                if data in random_szamok:
                    counter += 1
                    self.total += 1

            if counter == self.win:
                print(f'Total c3: {self.total}')



    @cache
    def core_4(self):
        while True:
            random_szamok = [random.randint(1, 99) for _ in range(5)]

            counter = 0
            for data in self.sajat_szamok:
                if data in random_szamok:
                    counter += 1
                    self.total += 1

            if counter == self.win:
                print(f'Total c4: {self.total}')


    def cores(self):
        self.c1 = multiprocessing.Process(target=self.core_1)
        self.c2 = multiprocessing.Process(target=self.core_2)
        self.c3 = multiprocessing.Process(target=self.core_3)
        self.c4 = multiprocessing.Process(target=self.core_4)


    def build(self):
        self.take_input()
        self.cores()

        self.c1.start()
        self.c2.start()
        self.c3.start()
        self.c4.start()

        self.c1.join()
        self.c2.join()
        self.c3.join()
        self.c4.join()


if __name__ == '__main__':
    ltt = Lotto()
    ltt.build()
