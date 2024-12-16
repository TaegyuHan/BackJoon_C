import sys


class Player:
    def __init__(self, power: int, life: int) -> None:
        self._power_point: int = power
        self._life_point: int = life
        self._is_alive: bool = True

    def attack(self, other: "Player") -> None:
        other._life_point -= self._power_point
        if other._life_point <= 0:
            other._is_alive = False

    @property
    def power_point(self) -> int:
        return self._power_point

    @property
    def is_alive(self) -> bool:
        return self._is_alive


class CardBoard:

    def __init__(self, a: Player, b: Player) -> None:
        self._a: Player = a
        self._b: Player = b

    def play(self):
        while self._a.is_alive and self._b.is_alive:
            self._a.attack(self._b)
            self._b.attack(self._a)

    def answer(self):
        if not self._a.is_alive and not self._b.is_alive:
            return "DRAW"
        if self._a.is_alive:
            return "PLAYER A"
        return "PLAYER B"


if __name__ == "__main__":
    # with open("1.txt", "r") as f:
    #     a_power, a_life = map(int, f.readline().split())
    #     b_power, b_life = map(int, f.readline().split())

    a_power, a_life = map(int, sys.stdin.readline().split())
    b_power, b_life = map(int, sys.stdin.readline().split())

    a: Player = Player(a_power, a_life)
    b: Player = Player(b_power, b_life)

    card_board: CardBoard = CardBoard(a, b)
    card_board.play()
    print(card_board.answer(), end="")