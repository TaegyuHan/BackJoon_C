"""
    Solution code for "BaekJoon 부분합".

    - Problem link: https://www.acmicpc.net/problem/1806
"""

from sys import stdin as input


class Pointer:
    """ 포인터 """

    def __init__(self):
        self.start = 0
        self.end = 0
        self.sum = D.NUM_LIST[self.start]
        self.length = 1

    def _diff(self):
        """ 두 길이 차이 """
        self.length = self.end - self.start + 1

    def move_start(self):
        """ 시작 포인터 움직이기 """
        self.sum -= D.NUM_LIST[self.start]
        self.start += 1
        self._diff()

    def move_end(self):
        """ 끝 포인터 움직이기 """
        self.end += 1
        self.sum += D.NUM_LIST[self.end]
        self._diff()

    def check_max(self):
        """ 값 확인하기 확인하기 """
        if self.sum >= D.MAX:
            return True
        return False

    def end_check(self):
        """ 포인터 움직임 끝났는지 확인 """
        if self.end == D.COUNT - 1 and not self.check_max():
            return False
        return True

class D:
    """ 데이터 """
    COUNT: int
    MAX: int
    NUM_LIST = []
    ANSWER = 0


class P:

    def __init__(self):
        D.COUNT, D.MAX = map(int, input.readline().split())
        D.NUM_LIST = list(map(int, input.readline().split()))
        D.ANSWER = D.COUNT
        self.pointer = Pointer()

    def run(self):
        """"""
        answer_chcek = False
        while self.pointer.end_check():

            if not self.pointer.check_max():
                self.pointer.move_end()
            else:
                answer_chcek = True
                D.ANSWER = min(D.ANSWER, self.pointer.length)
                self.pointer.move_start()

        if answer_chcek:
            print(D.ANSWER)
        else:
            print(0)

if __name__  == "__main__":
    # input = open("./1806.txt")
    P = P()
    P.run()