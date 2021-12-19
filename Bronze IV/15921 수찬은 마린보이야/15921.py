from sys import stdin as input

class P15921:

    def input_data(self):
        self.N = int(input.readline())
        self.count = {}
        if self.N:
            self.record_list = list(map(int, input.readline().split()))
            self.unique_list = set(self.record_list)

    def result(self):

        if self.N == 0:
            print("divide by zero")
            return

        expectations = 0
        average = sum(self.record_list) / self.N
        for num in self.unique_list:
            expectations += num * self.record_list.count(num) / self.N

        print("%.2f" %(average / expectations))


if __name__ == '__main__':
    # input = open('./15921.txt')
    P = P15921()
    P.input_data()
    P.result()