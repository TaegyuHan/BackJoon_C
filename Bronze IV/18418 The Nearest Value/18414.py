from sys import stdin as input

class P18414:

    def input_data(self):
        self.X, self.start, self.end = map(int, input.readline().split())

    def result(self):
        answer = sorted([self.X, self.start, self.end])
        print(answer[1])

if __name__ == '__main__':
    # input = open('./18414.txt')
    P = P18414()
    P.input_data()
    P.result()