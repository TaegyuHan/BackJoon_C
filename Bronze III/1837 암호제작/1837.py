from sys import stdin as input
from dataclasses import dataclass

class P:

    def __input_data(self) -> None:
        self.P, self.K = map(int, input.readline().split())

    @staticmethod
    def __prime_list(n) -> list[int]:
        """에라토스테네스의 체"""
        sieve = [True] * n
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i] == True:
                for j in range(i + i, n, i):
                    sieve[j] = False

        return [i for i in range(2, n) if sieve[i] == True]

    def __check_password(self, nums: list[int]) -> int:
        for num in nums:
            if self.P % num == 0:
                return num
        return 0

    def result(self) -> None:
        self.__input_data()
        prime_list = self.__prime_list(self.K)

        if answer := self.__check_password(prime_list):
            print("BAD", answer)
        else:
            print("GOOD")


if __name__ == '__main__':
    # input = open('./1837.txt')
    P = P()
    P.result()