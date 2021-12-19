from sys import stdin as input

class P21598:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        for _ in range(self.N):
            print("SciComLove")

if __name__ == '__main__':
    # input = open('./21598.txt')
    P = P21598()
    P.input_data()
    P.result()