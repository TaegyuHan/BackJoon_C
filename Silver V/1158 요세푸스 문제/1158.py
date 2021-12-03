from sys import stdin as input

class P1158:
    def __init__(self):
        self.answer = []

    def input_data(self):
        self.N, self.K = map(int, input.readline().split())
        self.number_list = [i for i in range(1, self.N + 1)]

    def result(self):
        idx = 0
        tmp = 0
        while self.number_list:
            tmp += 1

            if tmp == self.K:
                self.answer.append(self.number_list.pop(idx))
                idx -= 1
                tmp = 0

            idx += 1
            if len(self.number_list) <= idx:
                idx = 0

        print(f"<{', '.join(map(str, self.answer))}>")


if __name__ == '__main__':
    # input = open("./1158.txt")
    P = P1158()
    P.input_data()
    P.result()