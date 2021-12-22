from sys import stdin as input

class P2476:

    def input_data(self):
        self.TEST_COUNT = int(input.readline())

    def _check_prize_money(self):
        a, b, c = map(int, input.readline().split())
        if a == b and b == c and c == a:
            return a * 1_000 + 10_000
        elif a == b:
            return a * 100 + 1_000
        elif b == c:
            return b * 100 + 1_000
        elif c == a:
            return c * 100 + 1_000
        else:
            return max(a, b, c) * 100

    def result(self):
        answer = 0
        for _ in range(self.TEST_COUNT):
            if (tmp := self._check_prize_money()) > answer:
                answer = tmp
        print(answer)

if __name__ == '__main__':
    # input = open('./2476.txt')
    P = P2476()
    P.input_data()
    P.result()