from sys import stdin as input

class P20976:

    def input_data(self):
        self.number_list = sorted(map(int, input.readline().split()))

    def result(self):
        print(self.number_list[1])

if __name__ == '__main__':
    # input = open('./20976.txt')
    P = P20976()
    P.input_data()
    P.result()