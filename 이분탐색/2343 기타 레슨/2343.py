"""
    Solution code for "BaekJoon 기타 레슨".

    - Problem link: https://www.acmicpc.net/problem/2343
"""
from sys import stdin as input

# input = open('./2343.txt')


class D:
    """ 데이터 """
    N: int
    M: int
    CLASS_TIMES: list[int]

    @classmethod
    def input_data(cls):
        """ 데이터 받기 """
        cls.N, cls.M = map(int, input.readline().split())
        cls.CLASS_TIMES = list(map(int, input.readline().split()))

    @classmethod
    def sum_class_all_time(cls) -> int:
        """ 비디오 모든시간 """
        return sum(cls.CLASS_TIMES)

    @classmethod
    def low_class_time(cls) -> int:
        """ 가장 작은 시간 """
        return max(cls.CLASS_TIMES)

    @classmethod
    def check_time(cls, time: int) -> bool:
        """ 가능한 블루레이의 크기 확인 """
        tmp_sum = 0
        count = 1
        for class_time in cls.CLASS_TIMES:
            if tmp_sum + class_time > time:
                count += 1
                tmp_sum = class_time
                if count > cls.M:
                    return False
            else:
                tmp_sum += class_time
        if count > cls.M:
            return False
        return True


class P:

    @classmethod
    def _binary_search(cls):
        """ 이분탐색 """
        left = 1
        right = D.sum_class_all_time()
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if D.check_time(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        print(max(answer, D.low_class_time()))

    @classmethod
    def run(cls) -> None:
        """ 실행 """
        D.input_data()
        cls._binary_search()


if __name__ == '__main__':
    P.run()