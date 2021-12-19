from sys import stdin as input

class P20232:

    def input_data(self):
        self.winner_name = {
            0: "ITMO",
            1: "SPbSU",
            2: "PetrSU"
        }
        self.winner_list = [
            [0], [1], [1], [0], [0],
            [1], [0], [0], [0], [0],
            [0], [2, 0], [1], [1],
            [0], [0], [0], [0], [1],
            [0], [0], [0], [0], [1],
            [0]
        ]
        self.winner_year = int(input.readline())

    def result(self):
        tmp_winner = self.winner_list[self.winner_year - 1995]
        if len(tmp_winner) > 1:
            print(", ".join(map(lambda x: self.winner_name[x], tmp_winner)))
        else:
            print(self.winner_name[tmp_winner[0]])


if __name__ == '__main__':
    # input = open('./20232.txt')
    P = P20232()
    P.input_data()
    P.result()