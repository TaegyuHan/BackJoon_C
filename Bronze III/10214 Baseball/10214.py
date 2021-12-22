from sys import stdin as input

class P10214:

    def input_data(self):
        self.TEST_CASE = int(input.readline())
        self.INNING = 9

    def _win(self, yonsei, korea):
        if yonsei > korea:
            print("Yonsei")
        elif yonsei < korea:
            print("Korea")
        else:
            print("Draw")

    def result(self):
        for _ in range(self.TEST_CASE):
            yonsei = 0
            korea = 0
            for _ in range(self.INNING):
                y, k = map(int, input.readline().split())
                yonsei += y
                korea += k
            self._win(yonsei, korea)


if __name__ == '__main__':
    # input = open('./10214.txt')
    P = P10214()
    P.input_data()
    P.result()