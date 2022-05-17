"""
    Solution code for "BaekJoon 보석 도둑".

    - Problem link: https://www.acmicpc.net/problem/1202
"""

from sys import stdin as input
import heapq


class D:
    """ data """
    COUNT: int
    BAG: int
    JEWELRY = []
    BAG_SIZES = []
    ANSWER = 0

class P:

    def __init__(self) -> None:
        D.COUNT, D.BAG = map(int, input.readline().split())
        self._init_jewelry()
        D.BAG_SIZES = [int(input.readline()) for _ in range(D.BAG)]
        D.BAG_SIZES.sort()
        D.JEWELRY.sort()

    def _init_jewelry(self):
        """ 보석 받기 """
        for _ in range(D.COUNT):
            heapq.heappush(D.JEWELRY, tuple(map(int, input.readline().split())))

    def _push_bags(self):
        """ 가방 채우기 """
        max_heap = []
        for bag_size in D.BAG_SIZES:
            while D.JEWELRY and bag_size >= D.JEWELRY[0][0]:
                size, price = heapq.heappop(D.JEWELRY)
                heapq.heappush(max_heap, -price)

            if max_heap:
                D.ANSWER -= heapq.heappop(max_heap)
            elif not D.JEWELRY:
                break

    def run(self) -> None:
        self._push_bags()
        print(D.ANSWER)


if __name__ == '__main__':
    # input = open('./1202.txt')
    P = P()
    P.run()