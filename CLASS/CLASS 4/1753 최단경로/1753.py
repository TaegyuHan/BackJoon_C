"""
    Solution code for "BaekJoon 최단경로".

    - Problem link: https://www.acmicpc.net/problem/1753

    # 메모리 초과
"""
from sys import stdin as input
from sys import maxsize as InF
import heapq


class D:
    """ Data """
    NODE: int
    EDGE: int
    GO_NODE: int
    GRAPH = []
    PATH = []


class P:

    def __init__(self) -> None:
        D.NODE, D.EDGE = map(int, input.readline().split())
        D.GO_NODE = int(input.readline())
        self._init_graph()

    def _init_graph(self):
        """ 그래프 데이터 받기 """
        for i in range(D.NODE):
            D.GRAPH.append([(0, i)])

        for _ in range(D.EDGE):
            go, end, weight = map(int, input.readline().split())
            D.GRAPH[go - 1].append((weight, end - 1))

        # 정답 저장
        D.PATH = [InF for _ in range(D.NODE)]

    def _dijkstra(self):
        """ 다익스트라 알고리즘 실행 """
        strat_node = (0, D.GO_NODE - 1)
        queue = []
        heapq.heappush(queue, strat_node)

        while queue:
            weight, current_node = heapq.heappop(queue)

            for next_node_weight, next_node in D.GRAPH[current_node]:

                tmp_weight = weight + next_node_weight

                # 기존보다 크면 pass
                if D.PATH[next_node] <= tmp_weight: continue

                D.PATH[next_node] = tmp_weight
                heapq.heappush(queue, (tmp_weight, next_node))

    def _answer(self):
        """ 정답 출력 """
        for answer in D.PATH:
            if answer == InF: print("INF")
            else: print(answer)

    def run(self) -> None:
        """ 코드 실행 """
        self._dijkstra()
        self._answer()

if __name__ == '__main__':
    # input = open('./1753.txt')
    P = P()
    P.run()