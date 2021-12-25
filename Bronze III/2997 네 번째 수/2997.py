from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.n1, self.n2, self.n3 = sorted(map(int, input.readline().split()))

    @staticmethod
    def __find_d(n1: int, n2: int, n3: int) -> int:
        return min(n2 - n1, n3 - n2)

    @staticmethod
    def __check(num_tuple: tuple[int], d: int) -> int:
        frist_num = num_tuple[0]
        for i in range(1, 3):
            if (tmp := frist_num + ((i) * d)) != num_tuple[i]:
                return tmp

        if (frist_num + d) < 100:
            return num_tuple[2] + d
        else:
            return frist_num - d

    def result(self) -> None:
        self.__input_data()
        d = self.__find_d(self.n1, self.n2, self.n3)
        answer = self.__check((self.n1, self.n2, self.n3), d)
        print(answer)


if __name__ == '__main__':
    # input = open('./2997.txt')
    P = P()
    P.result()