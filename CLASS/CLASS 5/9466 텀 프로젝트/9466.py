"""Solution code for "BaekJoon ???. ???".

- Problem link: https://www.acmicpc.net/problem/???
"""
from sys import stdin as input
from collections import deque


class S:
    """ 상태 """
    ZERO = 0


class D:
    """ 데이터 """
    TEST_CASE: int # 2
    NODE_COUNT: int # 7
    NODE_DIRECTION = []
    NODE_DIRECTION_COUNT = [] # < 0 들어감
    ANSWER: int # 7


class P:

    def __init__(self) -> None:
        D.TEST_CASE = int(input.readline())

    def _input_test_data(self):
        """ 테스트 데이터 받기 """
        D.NODE_COUNT = int(input.readline())
        D.ANSWER = 0
        D.NODE_DIRECTION_COUNT = [0 for _ in range(D.NODE_COUNT + 1)]
        input_nodes = list(map(int, input.readline().split()))
        D.NODE_DIRECTION = [0] + input_nodes
        for node_direction in input_nodes:
            D.NODE_DIRECTION_COUNT[node_direction] += 1

    def _find_first_zero_node(self):
        """ 첫번째 0인 노드 찾기  """
        zero_nodes = []
        for index, node_count in enumerate(D.NODE_DIRECTION_COUNT):
            if index == S.ZERO: continue
            if node_count != S.ZERO: continue
            zero_nodes.append(index)
        return zero_nodes

    def _topological_sorting(self):
        """ 위상정렬 이용 """
        self._input_test_data() # 데이터 넣기
        zero_nodes = self._find_first_zero_node()
        q = deque(zero_nodes)

        while q:
            current_node = q.popleft()
            D.ANSWER += 1
            next_node = D.NODE_DIRECTION[current_node]
            D.NODE_DIRECTION_COUNT[next_node] -= 1

            if D.NODE_DIRECTION_COUNT[next_node] == S.ZERO:
                q.append(next_node)

    def _test_run(self):
        """ 테스트 실행 하기"""
        for _ in range(D.TEST_CASE):
            self._topological_sorting()
            print(D.ANSWER)

    def result(self) -> None:
        self._test_run()


if __name__ == '__main__':
    #input = open('./9466.txt')
    P = P()
    P.result()