# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.MAX = 1_000_000
        self.PN = [True for _ in range(self.MAX)]

    def _input_date(self) -> None:
        """데이터 받기"""
        self.N = int(input.readline())
        return self.N

    def _sieve_of_eratosthenes(self) -> None:
        """에라토스테네스 체"""
        for i in range(2, int(self.MAX*0.6)):
            if self.PN[i] == True:
                 for j in range(i*2, self.MAX, i):
                     if self.PN[j] == True: self.PN[j] = False

    def result(self) -> None:
        """결과"""
        self._sieve_of_eratosthenes()
        while self._input_date() != 0:
            print_check = True
            for i in range(3, self.MAX):
                if self.PN[i] == True and self.PN[self.N - i] == True:
                    print(f"{self.N} = {i} + {self.N - i}")
                    print_check = False
                    break
            if print_check:
                print("Goldbach's conjecture is wrong.")


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    input = open('./6588.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)