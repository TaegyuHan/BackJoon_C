"""
    Solution code for "BaekJoon 소수의 연속합".

    - Problem link: https://www.acmicpc.net/problem/1644
"""
import sys
from sys import stdin as input


class Pointer:
    """ 포인터 구현 """

    def __init__(self, num, num_list):
        """ 생성자 """
        self.num = num
        self._num_list = num_list
        self.start = 0
        self.end = 0
        self.sum = self._num_list[self.start]
        self.chcek_end = len(self._num_list) - 1
        self.answer = 0

    def _same_num_check(self):
        """ 숫자가 같은지 확인 """
        if self.sum == self.num:
            self.answer += 1
            return
        return

    def move_type_check(self):
        """ 움직이는 타입 체크 """
        if self.sum >= self.num:
            return True
        return False

    def move_start(self):
        """ 포인터 시작 움직이기 """
        self._same_num_check()
        self.sum -= self._num_list[self.start]
        self.start += 1

    def move_end(self):
        """ 포인터 시작 움직이기 """
        self.end += 1
        self.sum += self._num_list[self.end]
        self._same_num_check

    def end_check(self):
        """ 포인터가 끝났는지 확인 """
        if self.end > self.chcek_end:
            return False

        if self.end == self.chcek_end \
                and self.sum < self.num:
            return False
        return True


class PrimeNumber:
    """ 소수 판별 클래스 """

    def __init__(self, num):
        self.num = num
        self.prime_list = []
        self._init_prime_number()

    def _init_prime_number(self):
        """ 프라임 숫자 생성하기 """
        number_check = [False, False]
        number_check.extend([True for i in range(self.num - 1)])

        for i in range(2, self.num + 1):
            if not number_check[i]: continue
            self.prime_list.append(i)
            for j in range(i*2, self.num + 1, i):
                number_check[j] = False

    def prime_number_list(self):
        """ 소수 리스트 """
        return self.prime_list


class P:

    def __init__(self) -> None:
        num = int(input.readline())
        if num == 1:
            print(0)
            sys.exit()

        self.PN = PrimeNumber(num)
        self.Pointer = Pointer(num=num,
                               num_list=self.PN.prime_number_list())

    def run(self) -> None:
        """ 실행 """
        while self.Pointer.end_check():
            if self.Pointer.move_type_check():
                self.Pointer.move_start()
            else:
                self.Pointer.move_end()

        print(self.Pointer.answer)


if __name__ == '__main__':
    # input = open('./1644.txt')
    P = P()
    P.run()