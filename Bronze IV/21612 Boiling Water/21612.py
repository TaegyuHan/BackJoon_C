from sys import stdin as input

class P21612:

    def input_data(self):
        self.B = int(input.readline())

    def result(self):
        P = 5 * self.B - 400
        TMP = 100
        print(P)
        if  P < TMP:
            print(1)
        elif  P > TMP:
            print(-1)
        else:
            print(0)

if __name__ == '__main__':
    # input = open('./21612.txt')
    P = P21612()
    P.input_data()
    P.result()