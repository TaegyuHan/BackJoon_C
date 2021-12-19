from sys import stdin as input

class P21185:

    def input_data(self):
        self.N = int(input.readline())

    def result(self):
        if self.N%2 == 1:
            print("Either")
        elif self.N%4 == 0:
            print("Even")
        else:
            print("Odd")

if __name__ == '__main__':
    # input = open('./21185.txt')
    P = P21185()
    P.input_data()
    P.result()