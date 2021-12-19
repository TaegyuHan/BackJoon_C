from sys import stdin as input

class P21633:

    def input_data(self):
        self.k = int(input.readline())

    def result(self):
        cash = 25.0 + self.k * 0.01
        answer = min(max(cash, 100.00), 2000.00)
        print("%.2f" %answer)

if __name__ == '__main__':
    # input = open('./21633.txt')
    P = P21633()
    P.input_data()
    P.result()