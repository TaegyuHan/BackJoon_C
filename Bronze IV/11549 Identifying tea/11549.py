from sys import stdin as input

class P11549:

    def input_data(self):
        self.tea_number = int(input.readline())
        self.tea_list = list(map(int, input.readline().split()))

    def result(self):
        answer = 0
        for tea in self.tea_list:
            if self.tea_number == tea:
                answer += 1
        print(answer)

if __name__ == '__main__':
    # input = open('./11549.txt')
    P = P11549()
    P.input_data()
    P.result()