"""
    Solution code for "BaekJoon 놀이 공원".

    - Problem link: https://www.acmicpc.net/problem/1561

    N: 아이들의 수
        - N (1 ≤ N ≤ 2,000,000,000)

    M: 놀이기구(1인승 놀이기구)의 수
        - M (1 ≤ M ≤ 10,000)


    - 모든 놀이기구는 각각 운행 시간이 정해져 있다.
    - 운행 시간이 지나면 탑승하고 있던 아이는 내리게 된다.
    - 놀이 기구가 비어 있으면 현재 줄에서 가장 앞에 서 있는 아이가 빈 놀이기구에 탑승한다.
    - 만일 여러 개의 놀이기구가 동시에 비어 있으면, 더 작은 번호가 적혀 있는 놀이기구를 먼저 탑승한다고 한다.

    - 줄의 마지막 아이가 타게 되는 놀이기구의 번호를 구하는 프로그램을 작성하시오.

"""
from sys import stdin as input
input = open('./1561.txt')


class D:
    """ 데이터 """
    N: int
    M: int
    play_times: list[int]

    @classmethod
    def input_data(cls):
        """ 데이터 받기 """
        cls.N, cls.M = map(int, input.readline().split())
        cls.play_times = list(map(int, input.readline().split()))
        if cls.N <= cls.M:
            print(cls.N)
            exit()

    @classmethod
    def max_time(cls) -> int:
        """ 가장 최대로 걸릴 시간 """
        return cls.N * max(cls.play_times)

    @classmethod
    def show_data(cls):
        """ 데이터 보여주기  """
        print(cls.N, cls.M)
        print(cls.play_times)

    @classmethod
    def check_people(cls, time: int) -> bool:
        """
            탑습 인원 초과 확인

        :param time: 운행 시간

        :return:
            기다리는 인원보다
                많거나 같으면 > True
                적으면 > False
        """
        count = 0  # 탑승 인원 저장
        for play_time in cls.play_times:
            count += time // play_time  # 현재 시간의 탈 수 있는 인원 더하기

            if time % play_time:  # 초과 되는경우 1 더하기
                count += 1

            if count >= cls.N:  # 타야하는 인원보다 많으면 중지
                print("count", count)
                return True
        print("count", count)
        return False

    @classmethod
    def answer(cls, time: int) -> int:
        """
            몇번째 놀이기구 인지 반환하기

        :param time: 운행시간

        :return: 몇번째 놀이기구
        """
        before_time = time - 1  # 1분 전
        count = 0  # 횟수 저장
        for play_time in cls.play_times:
            count += before_time // play_time  # 몫 횟수

            if before_time % play_time:  # 나머지 있는 경우
                count += 1  # 1 더함

        answer = 0  # 정답(몇 번 째 놀이기구?)
        for idx, play_time in enumerate(cls.play_times):

            if not before_time % play_time:  # 새로 놀이기구를 타야하는 경우
                count += 1
                answer = idx + 1  # < 정답

            if count >= cls.N:  # 번째 같거나 크면 중지
                return answer

        return answer


class P:

    @classmethod
    def _binary_search(cls) -> None:
        """ 이분 탐색 """
        low = 1
        height = D.max_time()  # 가장 긴 시간

        while low <= height:
            mid = (low + height) // 2
            print(low, mid, height)
            if D.check_people(mid):  # 주어진 시간보다 탑승 인원이 많은 경우
                height = mid - 1
                answer_time = mid  # 최적의 시간
            else:
                low = mid + 1

        print(answer_time)
        print(D.answer(answer_time))  # 몇 번째 놀이기구 인지 찾기

    @classmethod
    def run(cls) -> None:
        """ 실행 """
        D.input_data()
        cls._binary_search()


if __name__ == '__main__':
    P.run()