"""
    Solution code for "BaekJoon 이중 우선순위 큐".

    - Problem link: https://www.acmicpc.net/problem/7662
"""

import heapq # 힙 자료형
from sys import stdin as input


class S:
    """ State """
    INPUT = "I"
    POP = "D"
    MAX = "1"
    MIN = "-1"


class D:
    """ 데이터 """
    TEST_COUNT: int # 테스트 수


class P:

    def __init__(self) -> None:
        D.TEST_COUNT = int(input.readline())

    def _init_priority_queue(self):
        """ 우선순위 큐 생성하기 """
        input_data_count = int(input.readline())
        heap = []
        for _ in range(input_data_count):
            data_type, data = input.readline().split()

            if data_type == S.INPUT:
                heapq.heappush(heap, int(data))
            if data_type == S.POP: # 데이터 꺼내기
                if len(heap) == 0: continue

                if data == S.MAX: # 최대값 꺼내기
                    max_data, *heap = heapq.nlargest(len(heap), heap)
                elif data == S.MIN:
                    min_data, *heap = heapq.nsmallest(len(heap), heap)

        if len(heap) == 0:
            print("EMPTY")
        else:
            max_data, *_ = heapq.nlargest(len(heap), heap)
            min_data, *_ = heapq.nsmallest(len(heap), heap)
            print(max_data, min_data)

    def run(self) -> None:
        for _ in range(D.TEST_COUNT):
            self._init_priority_queue()
            break


if __name__ == '__main__':
    # input = open('./7662.txt')
    P = P()
    P.run()
