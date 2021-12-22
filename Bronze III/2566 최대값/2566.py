from sys import stdin as input

class P2566:

    def input_data(self):
        self.BOARD_SIZE = 9
        self.board = []
        for _ in range(self.BOARD_SIZE):
            self.board.append(list(map(int, input.readline().split())))

    def result(self):
        answer = 0
        ri, ij = 0, 0
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.board[i][j] > answer:
                    answer = self.board[i][j]
                    ri, ij = i + 1, j + 1

        print(answer)
        print(ri, ij)


if __name__ == '__main__':
    # input = open('./2566.txt')
    P = P2566()
    P.input_data()
    P.result()