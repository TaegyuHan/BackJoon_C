from sys import stdin as input

class P20673:

    def input_data(self):
        self.P = int(input.readline())
        self.Q = int(input.readline())

    def result(self):
        if self.P <= 50 and self.Q <= 10:
            print("White")
        elif self.Q >= 30:
            print("Red")
        else:
            print("Yellow")

if __name__ == '__main__':
    # input = open('./20673.txt')
    P = P20673()
    P.input_data()
    P.result()