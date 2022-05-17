"""
    Solution code for "BaekJoon 트럭".

    - Problem link: https://www.acmicpc.net/problem/13335
"""

from sys import stdin as input
from collections import deque


class Bridge:
    """ 다리 """

    def __init__(self, size, weight):
        """ 다리 상태 """
        self._size = size
        self._weight = 0
        self._max_weight = weight
        self._q = deque([])

    def empty(self):
        """ 비엇는지 확인하기 """
        if not self._q:
            return True
        return False

    def enter(self, truck):
        """ 다리에 들어가기 """
        self._weight += truck
        self._q.append([self._size, truck])

    def out(self):
        """ 나오다 """
        if self._q and not self._q[0][0]:
            self._weight -= self._q.popleft()[1]

    def enter_check(self, truck):
        """ 들어갈 수 있는 지 확인 """
        if len(self._q) >= self._size:
            return False
        elif self._max_weight < self._weight + truck:
            return False
        return True

    def go(self):
        """ 다리에서 앞으로 가기 """
        for i in range(len(self._q)):
            self._q[i][0] -= 1

class P:

    def run(self) -> None:
        count, size, weight = map(int, input.readline().split())
        trucks = deque(list(map(int, input.readline().split())))
        bridge = Bridge(size, weight)

        time = 0
        while True:
            # 트럭이 전부 이동하면 중지
            if not trucks and bridge.empty(): break
            time += 1

            # 차 나오게 하기
            bridge.out()

            # 남아 있는 트럭이 있는 경우
            if trucks:
                if bridge.enter_check(trucks[0]): # 들어갈 수 있는지 확인
                    bridge.enter(trucks.popleft())

            # 차 앞으로 가기
            bridge.go()

        print(time)

if __name__ == '__main__':
    # input = open('./13335.txt')
    P = P()
    P.run()
