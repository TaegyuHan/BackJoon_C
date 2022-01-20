# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.N = 0

    def _input_date(self) -> None or int:
        """데이터 받는 메소드"""
        try:
            return int(input.readline())
        except ValueError as e:
            return

    def _find_digit(self) -> None:
        """자리수  찾는 메소드"""
        digit = 0
        answer = 1
        while True:
            digit = digit * 10 + 1
            digit %= self.N
            if digit == 0:
                print(answer)
                break
            answer += 1

    def result(self) -> None:
        """결과 출력 메소드"""
        while num := self._input_date():
            self.N = num
            self._find_digit()

if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./4375.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)