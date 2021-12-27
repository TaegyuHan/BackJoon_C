# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> int:
        self.n0 = int(input.readline())
        return self.n0

    def __calculation(self, i: int):
        answer = str(i) + ". "
        n1 = self.n0 * 3 # 1
        # 2
        if n1 % 2 == 0:
            n2 = n1 // 2
            answer += "even "
        else:
            n2 = (n1 + 1) // 2
            answer += "odd "
        # 3
        n3 = n2 * 3

        # 4
        n4 = n3 // 9
        answer += str(n4)
        print(answer)

    def result(self) -> None:
        i = 1
        while self.__input_data():
            self.__calculation(i)
            i += 1


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./4892.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)