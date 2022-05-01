"""
    Solution code for "BaekJoon 외계인의 기타 연주".

    - Problem link: https://www.acmicpc.net/problem/2841
"""

from sys import stdin as input


class Guitar:

    def __init__(self, data):
        self.sound, self._fret = data
        self._line = [[] for _ in range(7)]
        self._count = 0

    def show_press_line(self):
        """ 줄 누르고 있는 것 확인 """
        for row in self._line:
            print(row)

    def _line_last_fret(self, line):
        """ 라인의 마지막 플렛 """
        return self._line[line][-1]

    def press_line(self, line, fret):
        """ 줄 누르기 """

        # 줄을 안누르고 있는 경우
        if not len(self._line[line]):
            self._line[line].append(fret)
            self._count += 1
            return

        # 줄을 이미 누르고 있는 경우
        hold = self._line_last_fret(line)

        if hold == fret:
            return

        if fret > hold:
            self._line[line].append(fret)
            self._count += 1

        elif fret < hold:
            while fret < hold and self._line[line]:
                if self._line_last_fret(line) == fret: return
                if self._line_last_fret(line) < fret: break
                hold = self._line[line].pop()
                self._count += 1

            self._count += 1
            self._line[line].append(fret)
        else:
            return

    def answer(self):
        """ 정답 확인 """
        print(self._count)

class P:

    def run(self) -> None:
        G = Guitar(map(int, input.readline().split()))
        for _ in range(G.sound):
            line, fret = map(int, input.readline().split())
            G.press_line(line, fret)

        G.answer()


if __name__ == '__main__':
    # input = open('./2841.txt')
    P = P()
    P.run()