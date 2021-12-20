from sys import stdin as input

class P22279:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        answer = 0
        for _ in range(self.N):
            tmp1, tmp2 = map(float, input.readline().split())
            answer += tmp2 * tmp1
        print("%.3f" %answer)

if __name__ == '__main__':
    # input = open('./22279.txt')
    P = P22279()
    P.input_data()
    P.result()