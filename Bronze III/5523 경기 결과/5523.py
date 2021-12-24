from sys import stdin as input
from dataclasses import dataclass

@dataclass
class Win:
    A: int
    B: int

class P:

    def __init__(self):
        self.TEST_CASE = int(input.readline())

    def __input_data(self) -> None:
        return map(int, input.readline().split())

    @staticmethod
    def __chcek_win(Win: Win, A: int , B: int) -> Win:
        if A > B:
            Win.A += 1
        elif A < B :
            Win.B += 1
        return Win

    def result(self) -> None:
        W = Win(0, 0)
        for _ in range(self.TEST_CASE):
            A, B = self.__input_data()
            W = P.__chcek_win(W, A, B)

        print(W.A, W.B)

if __name__ == '__main__':
    # input = open('./5523.txt')
    P = P()
    P.result()