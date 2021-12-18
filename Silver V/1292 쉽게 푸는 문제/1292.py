from sys import stdin as input

class P1292:

    def input_data(self):
        self.A, self.B = map(int, input.readline().split())

    def result(self):
        answer = []
        for i in range(self.B + 1):
            for j in range(i):
                if len(answer) == self.B:
                    break
                answer.append(i)
        print(sum(answer[self.A - 1:self.B]))

if __name__ == '__main__':
    # input = open("./1292.txt")
    P = P1292()
    P.input_data()
    P.result()
