from sys import stdin as input

class P10103:

    def input_data(self):
        self.GAME_COUNT = int(input.readline())
        self.C_point, self.S_point = 100, 100

    def result(self):
        for _ in range(self.GAME_COUNT):
            C, S = map(int, input.readline().split())
            if C > S:
                self.S_point -= C
            elif C < S:
                self.C_point -= S

        print(self.C_point)
        print(self.S_point)

if __name__ == '__main__':
    # input = open('./10103.txt')
    P = P10103()
    P.input_data()
    P.result()