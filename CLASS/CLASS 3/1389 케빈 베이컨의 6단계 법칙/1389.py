"""
    Solution code for "BaekJoon 케빈 베이컨의 6단계 법칙".

    - Problem link: https://www.acmicpc.net/problem/1389
"""

from sys import stdin as input
from sys import maxsize


class S:
    """ 데이터 정보 """
    INF = "Inf"


class D:
    """ Data """
    NODE: int
    EDGE: int
    graph = []


class P:

    def __init__(self) -> None:
        D.NODE, D.EDGE = map(int, input.readline().split())
        self._init_graph()
        self._init_edge()

    def _init_graph(self):
        """ 그래프 생성 """
        for row in range(D.NODE):
            tmp = []
            for col in range(D.NODE):
                tmp.append(maxsize)
                if row == col: tmp[col] = 0
            D.graph.append(tmp)

    def _init_edge(self):
        """ 친구 연결 선 받기 """
        for _ in range(D.EDGE):
            man1, man2 = map(lambda x: x - 1,
                map(int, input.readline().split()))
            D.graph[man1][man2] = 1
            D.graph[man2][man1] = 1

    def _floyd_warshall(self):
        """ 플로이드 와샬 알고리즘 """
        for tmp in range(D.NODE):
            for row in range(D.NODE):
                for col in range(D.NODE):
                    D.graph[row][col] = \
                        min(D.graph[row][col],
                            (D.graph[row][tmp] + D.graph[tmp][col]))

    def _find_answer(self):
        """ 가장 작은 번호 찾기 """
        answer = 0
        tmp_sum = maxsize
        for man_number, count in enumerate(D.graph):
            if sum(count) < tmp_sum:
                tmp_sum = sum(count)
                answer = man_number + 1
        return answer

    def _show_graph(self):
        """ 그래프 확인하기 """
        for row in D.graph:
            print("\t".join(map(str, row)))

    def run(self) -> None:
        self._floyd_warshall()
        # self._show_graph()
        print(self._find_answer())

if __name__ == '__main__':
    # input = open('./1389.txt')
    P = P()
    P.run()