from sys import stdin as input
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

class P5639:
    def __init__(self):
        self.pre_order = []

    def _input_data(self):
        while True:
            tmp = input.readline().rstrip()
            if tmp == "":
                break
            self.pre_order.append(int(tmp))

    def _post_order(self, start, end):
        if start > end:
            return

        root = self.pre_order[start]  # 루트 노드
        idx = start + 1

        # root보다 커지는 지점을 찾기
        while idx <= end:
            if self.pre_order[idx] > root:
                break
            idx += 1

        self._post_order(start + 1, idx - 1)  # 왼쪽
        self._post_order(idx, end)  # 오른쪽
        print(root)  # 후위 순회 root 마지막 출력

    def result(self):
        self._input_data()
        self._post_order(0, len(self.pre_order) - 1)

if __name__ == "__main__":
    # input = open("./5639.txt")
    P = P5639()
    P.result()
