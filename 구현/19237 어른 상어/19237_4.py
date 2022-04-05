"""

    Solution code for "BaekJoon 어른 상어".

    - Problem link: https://www.acmicpc.net/problem/19237

    요구사항 주요 로직

    1. 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
    2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동 > 자신의 냄새를 그 칸에 뿌린다.
    3. 냄새는 상어가 k번 이동하고 나면 사라진다.

    이동 요구 사항
    1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
    2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
    3. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.

    4. 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

"""

from sys import stdin as input


class P:

    # 상하 좌우 이동
    # input 받은 수치로 계산
    GO_ROW = [0, -1, 1, 0, 0]
    GO_COL = [0, 0, 0, -1, 1]

    def __init__(self) -> None:
        self.size, self.shark_count, self.semll = map(int, input.readline().split())
        self._init_shark_board()
        self.current_direction = [0] + list(map(int, input.readline().split()))
        self._init_priority()

    def _init_shark_board(self):
        """ 상어 보드 설정 하기 """
        self.shark_position = {}
        board = []
        for row in range(self.size):
            tmp = list(map(int, input.readline().split()))
            board.append(tmp)
            for col in range(self.size):
                if (shark := tmp[col]) == 0: continue
                self.shark_position[f"{row},{col}"] = shark

        self.board = {
            "number": board,
            "smell": [[0 for _ in range(self.size)] for _ in range(self.size)]
        }

    def _init_priority(self):
        """ 상어 우선순위 받기 """
        self.shark_priority = [[]]
        for _ in range(self.shark_count):
            tmp = [[0, 0, 0, 0, 0]]
            for _ in range(4):
                tmp.append([0] + list(map(int, input.readline().split())))
            self.shark_priority.append(tmp)

    def _show_shark_number(self):
        """ 상어 숫자 확인 """
        for row in self.board["number"]:
            print(" ".join(map(str, row)))
        print()

    def _show_smell(self):
        """ 상어 냄새 확인 """
        for row in self.board["smell"]:
            print(" ".join(map(str, row)))
        print()

    def _move_shark(self):
        """ 상어 이동하기 """
        next_shark_position = {}
        for row_and_col in self.shark_position.keys():
            row, col = map(int, row_and_col.split(","))
            number = self.shark_position[row_and_col]
            direction = self.current_direction[number]
            shark_go_check = False # 상어가 냄새 없는곳 찾았는지 확인

            for go_check in self.shark_priority[number][direction][1:]: # 해당 방향의 우선순위
                nrow, ncol = row + P.GO_ROW[go_check], col + P.GO_COL[go_check] # 다음 이동경로
                if not (0 <= nrow < self.size and 0 <= ncol < self.size): continue # 어항에 안에서 놀기
                if self.board["smell"][nrow][ncol] != 0: continue # 기존에 냄새가 있는지 확인

                # 다른 상어가 있는지 확인
                if (next_key := f"{nrow},{ncol}") in next_shark_position.keys(): # 상어가 만남
                    if next_shark_position[next_key] < number:
                        shark_go_check = True # 상어 움직임
                        break # 기존의 상어의 숫자가 작은경우

                next_shark_position[next_key] = number # 상어 이동
                self.current_direction[number] = go_check # 상어 이동 방향
                shark_go_check = True  # 상어 움직임
                break

            # 상어 갈곳을 못찾음
            # 다시 왔던길로 냄새 찾아 돌아감
            if not shark_go_check:
                for go_check in range(1, 5):
                    nrow, ncol = row + P.GO_ROW[go_check], col + P.GO_COL[go_check] # 상하좌우
                    if not (0 <= nrow < self.size and 0 <= ncol < self.size): continue  # 어항에 안에서 놀기
                    if self.board["number"][nrow][ncol] == number: # 자신이 왔던 곳 찾음

                        # 기존 왔던 곳으로 이동
                        next_shark_position[f"{nrow},{ncol}"] = number
                        self.current_direction[number] = go_check
                        break

        self.shark_position = next_shark_position

    def _push_smell(self):
        """ 냄새 뿌리기 """
        for row_and_col in self.shark_position.keys():
            row, col = map(int, row_and_col.split(","))
            self.board["smell"][row][col] = self.semll # 냄새 뿌리기
            self.board["number"][row][col] = self.shark_position[row_and_col] # 누구 냄새인지 확인

    def _reduction_smell(self):
        """ 냄새 감소 """
        for row in range(self.size):
            for col in range(self.size):
                if self.board["smell"][row][col] == 0: continue # 그냥 물이면 pass

                # 냄새 감소
                self.board["smell"][row][col] -= 1
                if self.board["smell"][row][col] == 0:
                    self.board["number"][row][col] = 0 # 냄새가 사라져 상어 번호 제거

    def run(self) -> None:
        """ 문제 풀이 """


        for i in range(1000):
            self._push_smell()
            self._move_shark()
            self._reduction_smell()

            if len(self.shark_position) == 1:
                print(i + 1)
                break

            if i == 10:
                print(self.shark_position)
                self._show_shark_number()
                self._show_smell()
                break

        if i == 999:
            print(-1)

if __name__ == '__main__':
    input = open('./19237.txt')
    P = P()
    P.run()