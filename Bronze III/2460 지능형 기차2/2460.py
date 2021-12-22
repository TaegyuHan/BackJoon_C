from sys import stdin as input

class P2460:

    def input_data(self):
        self.TRAIN_STATIONS_COUNT = 10

    def result(self):
        answer = 0
        person = 0
        for _ in range(self.TRAIN_STATIONS_COUNT):
            out_p, in_p = map(int, input.readline().split())
            person -= out_p
            person += in_p
            if person > answer:
                answer = person
        print(answer)


if __name__ == '__main__':
    # input = open('./2460.txt')
    P = P2460()
    P.input_data()
    P.result()
