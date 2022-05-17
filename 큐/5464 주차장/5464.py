"""
    Solution code for "BaekJoon 주차장".

    - Problem link: https://www.acmicpc.net/problem/5464
"""
from sys import stdin as input
from collections import deque

class P:

    def run(self) -> None:
        car_park_count, car_count = map(int, input.readline().split())
        parks = set(i for i in range(car_park_count))
        car_position = {}
        pirces = [int(input.readline()) for _ in range(car_park_count)]
        car_weight = [int(input.readline()) for _ in range(car_count)]
        wait = deque([])
        answer = 0

        for _ in range(car_count*2):
            car = int(input.readline())

            if car > 0: # 차가 들어오는 경우
                if parks: # 주차 공간이 있는경우
                    location = min(parks)
                    answer += pirces[location]*car_weight[car - 1]
                    parks.remove(location)
                    car_position[car] = location
                else: # 주차 공간이 없는 경우
                    wait.append(car)

            else: # 차가 나가는 경우
                car = abs(car)
                location = car_position[car]
                del car_position[car]
                parks.add(location)

                if wait:
                    next_car = wait.popleft()
                    answer += pirces[location] * car_weight[next_car - 1]
                    parks.remove(location)
                    car_position[next_car] = location

        print(answer)

if __name__ == '__main__':
    # input = open('./5464.txt')
    P = P()
    P.run()
