from sys import stdin as input

class P5717:

    def input_data(self):
        while True:
            a, b = map(int, input.readline().split())
            if a == 0 and b == 0:
                break
            print(a + b)

    def result(self):
        pass

if __name__ == '__main__':
    # input = open('./5717.txt')
    P = P5717()
    P.input_data()
    P.result()