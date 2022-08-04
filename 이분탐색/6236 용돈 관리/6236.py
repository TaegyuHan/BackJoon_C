"""
    Solution code for "BaekJoon 용돈 관리".

    - Problem link: https://www.acmicpc.net/problem/6236
"""
from sys import stdin as input

# input = open('./6236.txt')


class D:
    """ 데이터 """
    _N: int
    _M: int
    _prices: list[int]

    @classmethod
    def input_data(cls):
        """ 데이터 받기 """
        cls._N, cls._M = map(int, input.readline().split())
        cls._prices = [int(input.readline()) for _ in range(cls._N)]

    @classmethod
    def sum_price(cls):
        """ 최대 돈 """
        return sum(cls._prices)

    @classmethod
    def max_price(cls):
        """ 최소 돈 """
        return max(cls._prices)

    @classmethod
    def check_money(cls, take_out_money: int) -> bool:
        """ 돈 확인하기 """
        balance = 0
        count = 1

        for today in cls._prices:
            balance += today
            if balance > take_out_money:
                balance = today
                count += 1

        return count <= cls._M


class P:

    @classmethod
    def _binary_search(cls):
        """ 이분탐색 """
        left = D.max_price()
        right = D.sum_price()
        while left < right:
            mid = (left + right) // 2
            if D.check_money(mid):
                right = mid
            else:
                left = mid + 1
        print(right)

    @classmethod
    def run(cls) -> None:
        """ 실행 """
        D.input_data()
        cls._binary_search()
        pass


if __name__ == '__main__':
    P.run()
