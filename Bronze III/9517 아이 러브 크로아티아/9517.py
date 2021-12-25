from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.MAN_COUNT = 8
        self.current_man = int(input.readline())
        self.QUESTION_COUNT = int(input.readline())
        self.MAX_TIME = 210
        self.time = 0

    def __check_man_count(self) -> None:
        if self.current_man % 8:
            self.current_man = self.current_man % 8
        else:
            self.current_man = 8

    def __check_time(self) -> None:
        if self.MAX_TIME <= self.time:
            return True
        else:
            return False

    def __check_answer(self, answer) -> None:
        if answer == "T":
            self.current_man += 1
        else:
            pass

    def result(self) -> None:
        self.__input_data()
        for _ in range(self.QUESTION_COUNT):
            time, answer = input.readline().split()

            # 시간 확인
            self.time += int(time)
            if self.__check_time(): break

            # 정답 확인
            self.__check_answer(answer)

        self.__check_man_count()
        print(self.current_man)


if __name__ == '__main__':
    # input = open('./9517.txt')
    P = P()
    P.result()