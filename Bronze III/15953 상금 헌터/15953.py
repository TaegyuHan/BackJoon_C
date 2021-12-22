from sys import stdin as input

class P15953:

    def input_data(self):
        self.TEST_COUNT = int(input.readline())

    def _festival_2017(self, rank):
        prize_money = 0
        if rank == 1:
            prize_money += 5_000_000
        elif 2 <= rank and rank <= 3:
            prize_money += 3_000_000
        elif 4 <= rank and rank <= 6:
            prize_money += 2_000_000
        elif 7 <= rank and rank <= 10:
            prize_money += 500_000
        elif 11 <= rank and rank <= 15:
            prize_money += 300_000
        elif 16 <= rank and rank <= 21:
            prize_money += 100_000

        return prize_money

    def _festival_2018(self, rank):
        prize_money = 0
        if rank == 1:
            prize_money += 5_120_000
        elif 2 <= rank and rank <= 3:
            prize_money += 2_560_000
        elif 4 <= rank and rank <= 7:
            prize_money += 1_280_000
        elif 8 <= rank and rank <= 15:
            prize_money += 640_000
        elif 16 <= rank and rank <= 31:
            prize_money += 320_000

        return prize_money

    def result(self):
        for _ in range(self.TEST_COUNT):
            P2017, P2018 = map(int, input.readline().split())
            total_prize_money = self._festival_2017(P2017) + self._festival_2018(P2018)
            print(total_prize_money)


if __name__ == '__main__':
    # input = open('./15953.txt')
    P = P15953()
    P.input_data()
    P.result()