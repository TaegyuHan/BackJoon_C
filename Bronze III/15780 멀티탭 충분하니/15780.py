# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.N, self.K = map(int , input.readline().split())
        self.multi_socket = map(int , input.readline().split())

    @staticmethod
    def __check_socket_count(socket: int) -> int:
        if socket % 2 == 0:
            return socket // 2
        else:
            return socket - (socket // 2)

    def __check_yes_or_no(self, totoal: int) -> None:
        if self.N > totoal:
            print("NO")
        else:
            print("YES")

    def result(self) -> None:
        totoal_socket_count = 0
        self.__input_data()
        for socket in self.multi_socket:
            totoal_socket_count += self.__check_socket_count(socket)

        self.__check_yes_or_no(totoal_socket_count)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./15780.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)