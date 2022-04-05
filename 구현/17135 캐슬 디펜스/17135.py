"""Solution code for "BaekJoon 캐슬 디펜스".

- Problem link: https://www.acmicpc.net/problem/17135
"""

from sys import stdin as input
from copy import deepcopy
from itertools import combinations
from collections import deque


class P:
    ARCHER_COUNT = 3

    def __init__(self) -> None:
        self.N, self.M, self.D = map(int, input.readline().split())
        self.archer_positions = list(combinations(range(self.M), P.ARCHER_COUNT))

        self.field = deque()
        self._init_field() # 필드 생성

        self.simulation_count = len(self.archer_positions)
        self._init_simulations() # 시뮬레이션 생성
        self._init_attack_distance() # 공격 가능 거리 생성
        self._init_attack_counts() # 시뮬레이션별 공격 횟수 생성

    def _init_attack_distance(self):
        """ 공격 가능 위치 생성 """
        self.attack_distances = []
        for i in range(self.simulation_count):
            tmp = []
            for col in self.archer_positions[i]:
                tmp.append(self._attack_distance_check(self.N, col))
            self.attack_distances.append(tmp)

    def _init_simulations(self):
        """ 궁수 배치별 시뮬레이션 생성 """
        self.simulations = []
        for _ in range(self.simulation_count):
            self.simulations.append(deepcopy(self.field))

    def _init_field(self):
        """ 필드 데이터 받이서 생성 """
        for _ in range(self.N):
            self.field.append(list(input.readline().split()))

    def _init_attack_counts(self):
        """ 궁수 공격 횟수 저장 """
        self.attack_counts = []
        for _ in range(self.simulation_count):
            self.attack_counts.append(0)

    def _show_simulations_field(self):
        """ 시뮬레이션 필드 확인 """
        for row in range(self.N):
            for i in range(self.simulation_count):
                print("|", " ".join(self.simulations[i][row]), end=" | ")
            print()

        for i in range(self.simulation_count):
            print("|", " ".join(["-" for _ in range(self.M)]), end=" | ")
        print()

        for i in range(self.simulation_count):
            tmp = []
            for col in range(self.M):
                if col in self.archer_positions[i]:
                    tmp.append("X")
                else:
                    tmp.append("O")
            print("|", " ".join(tmp), end=" | ")
        print()
        print()

    def _show_simulation_field(self, index: int):
        """ 특정 시뮬레이션 필드 확인 """
        for row in range(self.N):
                print(" ".join(self.simulations[index][row]))

        print(" ".join(["-" for _ in range(self.M)]))

        tmp = []
        for col in range(self.M):
            if col in self.archer_positions[index]:
                tmp.append("X")
            else:
                tmp.append("O")
        print(" ".join(tmp))
        print()
        print()

    def _show_field(self):
        """ 생성 필드 확인 """
        for row in self.field:
            print(" ".join(row))

    def _move_enemy(self):
        """ 적 성벽으로 이동 """
        for i in range(self.simulation_count):
            self.simulations[i].pop()
            self.simulations[i].appendleft(["0" for _ in range(self.M)])

    def _attack_distance_check(self, r1, c1):
        """ 공격 가능한 거리 인지 확인 """
        attack_distances = []
        for row in range(r1 - 1, r1 - self.D - 1, -1):
            for col in range(c1 - self.D + 1, c1 + self.D):

                # 필드 범위에 들어오는지 확인
                if not ((0 <= row < self.N) and (0 <= col < self.M)):
                    continue

                # 공격 가능한 거리 인지 확인
                distance = abs(row - r1) + abs(col - c1)
                if distance > self.D:
                    continue

                attack_distances.append((row, col, distance))

        return sorted(attack_distances, key=lambda x: (x[2], x[1], x[0])) # 가까운, 왼쪽 순으로 정렬

    def _archer_attack(self):
        """ 궁수 공격 """
        for i in range(self.simulation_count):

            tmp_attacks = set()
            # 공격할 적 찾기
            for attack_positions in self.attack_distances[i]:
                for attack_position in attack_positions:
                    row, col, distance = attack_position
                    if self.simulations[i][row][col] == '1':
                        tmp_attacks.add((row, col))
                        break

            # 동시에 공격
            for attack_position in tmp_attacks:
                row, col = attack_position
                self.simulations[i][row][col] = '0'

            # 공격 횟수
            self.attack_counts[i] += len(tmp_attacks)

    def run(self) -> None:
        for _ in range(self.N):
            self._archer_attack()
            self._move_enemy()

        print(max(self.attack_counts))
        pass


if __name__ == '__main__':
    # input = open('./17135.txt')
    P = P()
    P.run()