# import time
from sys import stdin as input
from dataclasses import dataclass

class P:

    def __init__(self) -> None:
        self.MAX_CHECK_NUMBER: int = 1_000_001

        self.current_channel: int = 100
        self.goal_channel: int = int(input.readline())
        self.answer: int = \
            abs(self.current_channel - self.goal_channel)

        # 고장난 버튼 받기
        self.broken_button_count: int = int(input.readline())
        self.broken_buttons: set = set()

        # 고장난게 있을 경우
        if self.broken_button_count != 0:
            self.broken_buttons |= set(input.readline().split())

    def result(self) -> None:
        for all_num in range(self.MAX_CHECK_NUMBER):
            for i, num in enumerate(str(all_num)):
                all_not_broken_buttons = True
                # 해당 버튼의 고장난 버튼이 있으면 skip
                if num in self.broken_buttons:
                    all_not_broken_buttons = False
                    break

            # 고장난 버튼이 없을 경우
            if all_not_broken_buttons == True:
                # 답 찾는 부분
                self.answer = min(
                    self.answer, # 기존의 최소 값
                    # 버튼 누른수 + (+, -) 누른 횟수
                    len(str(all_num)) + abs(all_num - self.goal_channel)
                )

        print(self.answer)


if __name__ == '__main__':
    # start = time.time()  # 시작 시간 저장
    # input = open('./1107.txt')
    P = P()
    P.result()
    # print("time :", time.time() - start)