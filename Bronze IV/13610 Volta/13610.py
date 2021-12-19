from sys import stdin as input

class P13610:

    def input_data(self):
        self.X, self.Y = map(int, input.readline().split())

    def result(self):
        count = 1

        while True:
            if self.Y*count - self.X*count >= self.Y:
                # Y의 주행거리 - X의 주행거리 >= Y가 X에게 한바퀴 이상 추월당함
                break
            count += 1
        print(count)

if __name__ == '__main__':
    # input = open('./13610.txt')
    P = P13610()
    P.input_data()
    P.result()