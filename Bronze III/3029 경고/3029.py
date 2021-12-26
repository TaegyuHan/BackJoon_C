# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.current_time = input.readline()
        self.action_time = input.readline()

    @staticmethod
    def __change_time_to_seconde(time: str) -> int:
        hour, minute, second = map(int, time.split(":"))
        return (hour * 3_600) + (minute * 60) + second

    @staticmethod
    def __change_seconde_to_time(second: int) -> tuple: # tuple(int)
        hour = second // 3_600
        minute = (second % 3_600) // 60
        second = second % 60
        return hour, minute, second

    @staticmethod
    def __show_time(time: tuple):
        print(f"{time[0]:02d}:{time[1]:02d}:{time[2]:02d}")

    @staticmethod
    def __calculation_time(current: int, action: int) -> int:
        DAY_SECOND = 86_400
        if current >= action:
            action += DAY_SECOND
            term = action - current
        else:
            term = action - current
        return term

    def result(self) -> None:
        self.__input_data()
        current = self.__change_time_to_seconde(self.current_time)
        action = self.__change_time_to_seconde(self.action_time)
        term_seconde = self.__calculation_time(current, action)
        term_time = self.__change_seconde_to_time(term_seconde)
        self.__show_time(term_time)

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./3029.txt')
    P = P()
    P.result()
    # print(f"{time.time() - start:.10f} sec")