from sys import stdin as input

class P21591:

    def input_data(self):
        ( self.computer_w, self.computer_h,
          self.sticher_w, self.sticher_h ) = map(int, input.readline().split())

    def result(self):
        if self.computer_w - self.sticher_w >= 2 and \
            self.computer_h - self.sticher_h >= 2:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    # input = open('./21591.txt')
    P = P21591()
    P.input_data()
    P.result()