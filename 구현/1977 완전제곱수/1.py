import math
import sys


class PerfectSquareNumberFinder:

    def __init__(self, start_number: int, end_number: int) -> None:
        self._start_number: int = start_number
        self._end_number: int = end_number
        self._check_sum: int = 0
        self._check_min: int = 0

    def find(self) -> None:

        is_min: bool = True
        for num in range(self._start_number, self._end_number + 1):
            sqrt_num: float = math.sqrt(num)

            # 완전제곱수 확인
            if not self._check_number_type(sqrt_num):
                continue

            # 최솟값 확인
            if is_min:
                is_min = False
                self._check_min = num

            self._check_sum += num

    @staticmethod
    def _check_number_type(num: float) -> bool:
        if not isinstance(num, float):
            return False
        if num.is_integer():
            return True
        return False

    def answer(self) -> str:
        if self._check_sum == 0:
            return "-1"
        return f"{self._check_sum}\n{self._check_min}"


if __name__ == "__main__":
    # with open("1.txt", "r") as f:
    #     n: int = int(f.readline())
    #     m: int = int(f.readline())

    n: int = int(sys.stdin.readline())
    m: int = int(sys.stdin.readline())

    finder = PerfectSquareNumberFinder(n, m)
    finder.find()
    print(finder.answer(), end="")
