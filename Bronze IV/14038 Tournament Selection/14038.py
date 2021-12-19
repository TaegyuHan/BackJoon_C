from sys import stdin as input

class P14038:

    def input_data(self):
        self.W_count = 0
        for _ in range(6):
            tmp = input.readline().rstrip()
            if tmp == 'W':
                self.W_count += 1

    def result(self):
        if self.W_count >= 5:
            print(1)
        elif self.W_count >= 3:
            print(2)
        elif self.W_count >= 1:
            print(3)
        else:
            print(-1)

if __name__ == '__main__':
    # input = open('./14038.txt')
    P = P14038()
    P.input_data()
    P.result()