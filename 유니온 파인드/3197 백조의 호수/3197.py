"""
    Solution code for "BaekJoon 백조의 호수".

    - Problem link: https://www.acmicpc.net/problem/3197
"""
from sys import stdin as input
from collections import deque
import sys; sys.setrecursionlimit(2500)
# input = open('./3197.txt')


class M:
    """ 이동 """
    GO = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]


class D:
    """ 데이터 """
    ROW = 0
    COL = 0

    board = []
    nodes = []
    visited = []

    day = 0

    SWANS = []
    SWAN = "L"
    ICE = "X"
    WATER = "."
    queues = {}

    @staticmethod
    def show_board(board):
        """ 보여주기 """
        for row in board:
            print(*row, sep="\t")
        print()

    @staticmethod
    def show_nodes():
        """ 노드 보여주기 """
        for row in range(0, D.ROW):
            tmp = row * D.COL
            print(*D.nodes[tmp:tmp + D.COL], sep="\t")
        print()

    @staticmethod
    def arry_to_node(row, col):
        """ 배열 노드로 변경 """
        return (row * D.COL) + col

    @staticmethod
    def show_deque(queues):
        """ 큐 확인하기 """
        for key, nodes in queues.items():
            print(key, nodes)
        print()

    @staticmethod
    def node_to_arry(node_index):
        """ 노드 배열로 변경 """
        row = node_index // D.COL
        col = node_index % D.COL
        return row, col


class P:

    def __init__(self) -> None:
        """ 데이터 받기 """
        D.ROW, D.COL = map(int, input.readline().split())
        for row in range(D.ROW):
            row_tmp = list(input.readline().strip())
            D.board.append(row_tmp)
            D.visited.append([0] * D.COL)
            for col in range(D.COL):
                node_number = (row * D.COL) + col
                D.nodes.append(node_number)
                if row_tmp[col] == D.SWAN:
                    D.SWANS.append(node_number)

    def _bfs(self, row, col):
        """ 우선 넓이 탐색 """
        q = deque([(row, col)])
        rnode = D.arry_to_node(row, col)
        D.queues[rnode] = set()

        while q:
            crow, ccol = q.popleft()
            cnode = D.arry_to_node(crow, ccol)

            if D.visited[crow][ccol]:
                continue

            if D.board[crow][ccol] == D.ICE:
                D.queues[rnode].add(cnode)
                continue

            D.visited[crow][ccol] = 1
            if self._find(rnode) != self._find(cnode):
                self._union(rnode, cnode)

            for trow, tcol in M.GO:
                nrow, ncol = crow + trow, ccol + tcol
                if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                    continue
                elif D.visited[nrow][ncol]:
                    continue
                q.append((nrow, ncol))

    def _union(self, node1, node2, next_check=None):
        """ 합치기 """
        pnode1 = self._find(node1)
        pnode2 = self._find(node2)

        nodes = {pnode1, pnode2}
        if D.SWANS[0] in nodes: # 첫번째 백조 존재
            if D.SWANS[1] in nodes: # 백조 둘이 만남
                # 종료
                print(D.day)
                exit(0)
            D.nodes[pnode1] = D.SWANS[0]
            D.nodes[pnode2] = D.SWANS[0]
            return

            # 첫번째 백조만 만남
        elif D.SWANS[1] in nodes:
            if D.SWANS[0] in nodes: # 백조 둘이 만남
                # 종료
                print(D.day)
                exit(0)
            # 두번째 백조만 만남
            D.nodes[pnode1] = D.SWANS[1]
            D.nodes[pnode2] = D.SWANS[1]
            return

        if pnode1 > pnode2:
            D.nodes[pnode1] = pnode2
        else:
            D.nodes[pnode2] = pnode1

    def _find(self, node):
        """ root 노드 찾기 """
        if D.nodes[node] == node:
            return node

        D.nodes[node] = self._find(D.nodes[node])
        return D.nodes[node]

    def _make_nodes(self):
        """ 노드 생성 """
        # 백조 노드 만들기
        for row, col in map(D.node_to_arry, D.SWANS):
            self._bfs(row, col)

        # 물 노드 만들기
        for row in range(D.ROW):
            for col in range(D.COL):
                if D.visited[row][col]:
                    continue
                elif D.board[row][col] == D.ICE:
                    continue
                self._bfs(row, col)

    def _melting_ice(self):
        """ 얼음 녹이기 """
        while any(D.queues):
            tmp = {}
            D.day += 1

            for rnode, cnodes in D.queues.items():
                for cnode in cnodes:
                    crow, ccol = D.node_to_arry(cnode)
                    if D.visited[crow][ccol]:
                        continue
                    D.visited[crow][ccol] = 1

                    # 녹이기
                    if self._find(rnode) != self._find(cnode):
                        self._union(rnode, cnode)
                    D.board[crow][ccol] = D.WATER

                    for trow, tcol in M.GO:
                        nrow, ncol = crow + trow, ccol + tcol
                        if not (0 <= nrow < D.ROW and 0 <= ncol < D.COL):
                            continue

                        # 물을 만난경우
                        nnode = D.arry_to_node(nrow, ncol)
                        if D.board[nrow][ncol] == D.WATER:
                            if self._find(rnode) != self._find(nnode):
                                self._union(rnode, nnode, next_check=True)
                            continue

                        # 얼음을 만난 경우
                        elif D.board[nrow][ncol] == D.ICE:
                            if D.visited[nrow][ncol]:
                                continue
                            if (key := self._find(rnode)) not in tmp:
                                tmp[key] = set()
                            tmp[key].add(nnode)
            D.queues = tmp

    def run(self) -> None:
        """ 실행 """
        self._make_nodes()
        self._melting_ice()

        # D.show_nodes()
        # D.show_board(D.board)
        # D.show_board(D.visited)


if __name__ == '__main__':
    P = P()
    P.run()