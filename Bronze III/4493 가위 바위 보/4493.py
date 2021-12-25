from sys import stdin as input
from dataclasses import dataclass

@dataclass
class Player:
    one: int
    two: int

class P:

    def __init__(self):
        self.TEST_CASE = int(input.readline())

    def __input_game_count(self) -> None:
        self.game_count = int(input.readline())

    def __input_game(self) -> None:
        self.player1_card, self.player2_card = input.readline().split()

    def __check_winner(self) -> None:
        p1, p2 = self.player1_card, self.player2_card
        if p1 == p2:
            return

        if p1 == "R":
            if p2 == "S":
                self.P.one += 1
                return
            elif p2 == "P":
                self.P.two += 1
                return
        elif p1 == "S":
            if p2 == "R":
                self.P.two += 1
                return
            elif p2 == "P":
                self.P.one += 1
                return
        elif p1 == "P":
            if p2 == "S":
                self.P.two += 1
                return
            elif p2 == "R":
                self.P.one += 1

    def __check_final_winner(self) -> None:
        if self.P.one > self.P.two:
            print("Player 1")
        elif self.P.one < self.P.two:
            print("Player 2")
        else:
            print("TIE")

    def result(self) -> None:
        for _ in range(self.TEST_CASE):
            self.__input_game_count()
            self.P = Player(0, 0)
            for _ in range(self.game_count):
                self.__input_game()
                self.__check_winner()

            self.__check_final_winner()


if __name__ == '__main__':
    # input = open('./4493.txt')
    P = P()
    P.result()