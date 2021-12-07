from sys import stdin as input


class P17247:

    def input_data(self):
        self.one_position = []
        self.map = []
        self.H, self.W = map(int, input.readline().split())

        for i in range(self.H):
            self.map.append(tmp := list(map(int, input.readline().split())))
            for j, check_one in enumerate(tmp):
                if check_one == 1:
                    self.one_position.append((i, j))

    def result(self):
        P1, P2 = self.one_position
        print(abs(P1[0] - P2[0]) + abs(P1[1] - P2[1]))


if __name__ == '__main__':
    # input = open("./17247.txt")
    P = P17247()
    P.input_data()
    P.result()