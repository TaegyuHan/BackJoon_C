from sys import stdin as input

class P2965:

    def input_data(self):
        self.A, self.B, self.C = map(int, input.readline().split())

    def _check_stop(self):
        left, right = self.B - self.A, self.C - self.B
        if left == 0 or right == 0:
            return False
        else:
            return True

    def _move(self):
        left, right = self.B - self.A, self.C - self.B
        if left < right:
            self.A = self.B
            self.B = self.B + 1
        else:
            self.C = self.B
            self.B = self.B - 1

    def result(self):
        answer = -1
        while self._check_stop():
            self._move()
            answer += 1
        print(answer)

if __name__ == '__main__':
    # input = open('./2965.txt')
    P = P2965()
    P.input_data()
    P.result()