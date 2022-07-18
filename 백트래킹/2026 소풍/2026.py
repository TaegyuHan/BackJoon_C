"""
    Solution code for "BaekJoon 소풍".

    - Problem link: https://www.acmicpc.net/problem/2026


    - N(K ≤ N ≤ 900)명의 학생 중
    - K(1 ≤ K ≤ 62)명의 학생들을 소풍에 보내려고 한다.

    - 고은이에게 친구 관계에
        대한 정보를 F(1 ≤ F ≤ 5,600)개를 주시며 K명을 선발

"""
from sys import stdin as input
# input = open('./2026.txt')


class D:
    """ 데이터 """
    K: int
    N: int
    F: int
    array_graph: list[list[int]]
    counnct_count: list[int]

    @classmethod
    def input_data(cls):
        """ 데이터 받기 """
        cls.K, cls.N, cls.F = map(int, input.readline().split())
        cls._make_graph()
        cls._connect_count()

    @classmethod
    def _make_graph(cls):
        """ 그래프 배열 만들기 """
        cls.array_graph = []
        for row in range(cls.N + 1):
            tmp = [0] * (cls.N + 1)
            tmp[row] = 1
            cls.array_graph.append(tmp)

        for _ in range(cls.F):
            node1, node2 = map(int, input.readline().split())
            cls.array_graph[node1][node2] = 1
            cls.array_graph[node2][node1] = 1

    @classmethod
    def _connect_count(cls):
        """ 연결 개수 확인 """
        cls.counnct_count = [0] * (cls.N + 1)
        for row in range(1, cls.N + 1):
            cls.counnct_count[row] = sum(cls.array_graph[row])

    @classmethod
    def show_data(cls):
        """ 데이터 보여주기 """
        print(cls.K, cls.N, cls.F)
        print(cls.counnct_count)
        for row in cls.array_graph:
            print(*row)

    @classmethod
    def can_people(cls):
        """ 가능한 사람 반환 """
        check_list = []
        for idx in range(len(cls.counnct_count)):
            if cls.counnct_count[idx] < cls.K:
                continue
            check_list.append(idx)
        return check_list

    @classmethod
    def break_depth(cls):
        """ 백트레킹 브레이크 """
        return cls.K

    @classmethod
    def check_node(cls, node):
        """ 확인해야 하는 노드 """
        check_list = []
        for i in range(cls.N + 1):
            if cls.array_graph[node][i]:
                check_list.append(i)
        return check_list

    @classmethod
    def depth_check(cls, cnode: int, check_list: list[int]):
        """ 백트레킹 들어가기 체크 """
        next_check_list = []
        count = 0
        for node in check_list:
            if cls.array_graph[cnode][node]:
                next_check_list.append(node)
                count += 1

        if count >= cls.K:
            return next_check_list
        return []

    @classmethod
    def first_check(cls, node: int):
        """ 첫번째 들어가는 노드 체크 """
        next_check_list = []
        for check in range(cls.N + 1):
            if cls.array_graph[node][check]:
                next_check_list.append(check)
        return next_check_list


class P:

    @classmethod
    def _backtracking(cls,
                      depth: int,
                      visited: set[int],
                      check_list: list[int],
                      answer: list[int]):
        """ 백트레킹 """
        if depth >= D.break_depth():
            cls.show_answer(answer)
            exit()

        for nnode in range(D.N + 1):
            if nnode in visited:
                continue
            elif not (next_check_list := D.depth_check(nnode, check_list)):
                continue

            cls._backtracking(
                depth=depth + 1,
                visited=visited | {nnode},
                check_list=next_check_list,
                answer=answer + [nnode]
            )

    @classmethod
    def show_answer(cls, answer: list[int]):
        """ 정답 출력 """
        for a in answer:
            print(a)

    @classmethod
    def run(cls) -> None:
        """ 실행 """
        D.input_data()
        D.show_data()

        check_list = D.can_people()
        for node in check_list:
            check_list = D.first_check(node)
            cls._backtracking(
                depth=1,
                visited={node}, # 1
                check_list=check_list,
                answer=[node]
            )
        print(-1)


if __name__ == '__main__':
    P.run()
