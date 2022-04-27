"""
    Solution code for "BaekJoon 공항".

    - Problem link: https://www.acmicpc.net/problem/10775
"""
from sys import stdin as input


class S:
    """ 상태 """
    NOT_CONNECTION = False
    CONNECTION = True
    FIRST_GATE = 1


class D:
    """ 데이터 """
    GATE_COUNT: int
    AIRPLAN_COUNT: int
    GATE_CONNECTION_CHECK = [] # 공항 연동 확인
    TIME_SHORT_GATE_FIND = []
    ANSWER = 0


class P:

    def __init__(self) -> None:
        D.GATE_COUNT = int(input.readline())
        D.AIRPLAN_COUNT = int(input.readline())
        D.GATE_CONNECTION_CHECK = [S.NOT_CONNECTION for _ in range(D.GATE_COUNT + 1)]
        D.TIME_SHORT_GATE_FIND = [gate_number for gate_number in range(D.GATE_COUNT + 1)]

    def _input_airplan(self):
        """ 비행기 도착 """
        airplan_gate_number = int(input.readline())
        check_gate = D.TIME_SHORT_GATE_FIND[airplan_gate_number]

        while check_gate >= S.FIRST_GATE:
            if D.GATE_CONNECTION_CHECK[check_gate] == S.NOT_CONNECTION:
                D.GATE_CONNECTION_CHECK[check_gate] = S.CONNECTION
                D.TIME_SHORT_GATE_FIND[airplan_gate_number] = check_gate
                D.ANSWER += 1
                return
            check_gate -= 1

        print(D.ANSWER)
        exit()

    def run(self) -> None:
        """ 실행 """
        for _ in range(D.AIRPLAN_COUNT):
            self._input_airplan()
        print(D.ANSWER)


if __name__ == '__main__':
    # input = open('./10775.txt')
    P = P()
    P.run()