"""
    Solution code for "BaekJoon 예산".

    - Problem link: https://www.acmicpc.net/problem/2512
"""
from sys import stdin as input

# input = open('./2512.txt')


class D:
    """ 데이터 """
    N: int
    BUDGETS: list[int]
    MAX_BUDGET: int

    @classmethod
    def input_data(cls):
        """ 데이터 받기 """
        cls.N = int(input.readline())
        cls.BUDGETS = list(map(int, input.readline().split()))
        cls.MAX_BUDGET = int(input.readline())

    @classmethod
    def max_budget(cls) -> int:
        """ 예산 최대 값 """
        return max(cls.BUDGETS)

    @classmethod
    def total_budget(cls, fix_budget: int) -> int:
        """ 총 예산 """
        sum_budget = 0
        for budget in cls.BUDGETS:
            if budget >= fix_budget:
                sum_budget += fix_budget
            else:
                sum_budget += budget

        # print(sum_budget)
        if sum_budget > cls.MAX_BUDGET:
            return True
        return False


class P:

    @classmethod
    def _binary_search(cls):
        """ 이분탐색 """
        low = 0
        height = D.max_budget()
        answer = 0
        while low <= height:
            mid = (low + height) // 2
            if D.total_budget(mid):
                height = mid - 1
            else:
                low = mid + 1
                answer = mid
            # print(low, height)
        print(answer)

    @classmethod
    def run(cls) -> None:
        """ 실행 """
        D.input_data()
        cls._binary_search()


if __name__ == '__main__':
    P.run()