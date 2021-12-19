from sys import stdin as input

class P6763:

    def input_data(self):
        self.a = int(input.readline())
        self.b = int(input.readline())

    def result(self):
        over = self.b - self.a
        if over >= 31:
            print("You are speeding and your fine is $500.")
        elif over > 20:
            print("You are speeding and your fine is $270.")
        elif over > 0:
            print("You are speeding and your fine is $100.")
        else:
            print("Congratulations, you are within the speed limit!")


if __name__ == '__main__':
    # input = open('./6763.txt')
    P = P6763()
    P.input_data()
    P.result()