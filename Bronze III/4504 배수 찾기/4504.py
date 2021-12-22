from sys import stdin as input

class P4504:

    def input_data(self):
        self.TEST_NUMBER = int(input.readline())

    def result(self):
        while tmp := int(input.readline()):
            check = tmp % self.TEST_NUMBER
            if check == 0:
                print(f"{tmp} is a multiple of {self.TEST_NUMBER}.")
            else:
                print(f"{tmp} is NOT a multiple of {self.TEST_NUMBER}.")


if __name__ == '__main__':
    # input = open('./4504.txt')
    P = P4504()
    P.input_data()
    P.result()