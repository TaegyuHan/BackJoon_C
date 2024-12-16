import sys


class Calc:
    def __init__(self, num1: int, num2: int) -> None:
        self._num1: int = num1
        self._num2: int = num2

    def add(self) -> int:
        return self._num1 + self._num2


if __name__ == "__main__":
    # with open("1.txt", "r") as f:
    #     a, b = map(int, f.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    calc = Calc(a, b)
    print(calc.add(), end="")
