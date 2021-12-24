from sys import stdin as input
from dataclasses import dataclass


@dataclass
class Box:
    size: int


class P:

    def input_data(self):
        self.TEST_CASE = int(input.readline())

    @staticmethod
    def __make_box_end(size):
        print("#" * size)

    @staticmethod
    def __make_box_mid(size):
        for _ in range(size - 2):
            print(f"#{'J' * (size - 2)}#")

    @staticmethod
    def make_box(size):
        P.__make_box_end(size)
        P.__make_box_mid(size)
        P.__make_box_end(size)

    @staticmethod
    def size_one():
        print("#")

    def result(self):
        for i in range(self.TEST_CASE):
            B = Box(int(input.readline()))
            if B.size == 1:
                P.size_one()
            else:
                P.make_box(B.size)
            if i != self.TEST_CASE - 1:
                print()


if __name__ == '__main__':
    # input = open('./5354.txt')
    P = P()
    P.input_data()
    P.result()