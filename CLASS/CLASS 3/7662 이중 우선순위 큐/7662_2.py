"""
    Solution code for "BaekJoon 이중 우선순위 큐".

    - Problem link: https://www.acmicpc.net/problem/7662
"""

from sys import stdin as input
from collections import defaultdict
import heapq # 힙 자료형


class S:
    """ State """
    INPUT = "I"
    POP = "D"
    MAX = "1"
    MIN = "-1"
    EMTPY = 0


class D:
    """ 데이터 """
    TEST_COUNT: int # 테스트 수


class P:

    def __init__(self) -> None:
        D.TEST_COUNT = int(input.readline())

    def _pop_heap(self, min_max_type):
        """ 최대힙 꺼내기 """
        if min_max_type == S.MAX:
            heap = self.max_heap
            key = -1

        elif min_max_type == S.MIN:
            heap = self.min_heap
            key = 1

        if len(heap) == S.EMTPY: return

        data = heapq.heappop(heap)

        if self.check_dict[str(key*data)] == S.EMTPY:
            while heap:
                data = heapq.heappop(heap)
                if self.check_dict[str(key*data)] > S.EMTPY:
                    self.check_dict[str(key*data)] -= 1
                    return data
        else:
            self.check_dict[str(key*data)] -= 1
        return data

    def _pop_check(self):
        """ 이미 빠진 데이터인지 확인해주기 """
        while (self.max_heap
               and self.check_dict[str(-self.max_heap[0])] == S.EMTPY):
            heapq.heappop(self.max_heap)

        while (self.min_heap
               and self.check_dict[str(self.min_heap[0])] == S.EMTPY):
            heapq.heappop(self.min_heap)

    def _init_priority_queue(self):
        """ 우선순위 큐 생성하기 """
        input_data_count = int(input.readline())
        self.check_dict = defaultdict(int)
        self.max_heap, self.min_heap = [], []

        for check_index in range(input_data_count):
            data_type, data = input.readline().split()

            if data_type == S.INPUT:
                self.check_dict[data] += 1
                heapq.heappush(self.min_heap, int(data))
                heapq.heappush(self.max_heap, -int(data))

            if data_type == S.POP: # 데이터 꺼내기
                if data == S.MAX: # 최대값 꺼내기
                    self._pop_heap(S.MAX)

                elif data == S.MIN: # 최소값 꺼내기
                    self._pop_heap(S.MIN)

        # 사용한 값 제거해주기
        self._pop_check()

        if not any(self.check_dict.values()):
            print("EMPTY")
        else:
            print(-self.max_heap[0], self.min_heap[0])

    def run(self) -> None:
        for _ in range(D.TEST_COUNT):
            self._init_priority_queue()


if __name__ == '__main__':
    input = open('./7662.txt')
    P = P()
    P.run()
