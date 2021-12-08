from sys import stdin as input

class P1120:

    def input_data(self):
        self.A, self.B = input.readline().split()

        # string_length_difference
        self.sld = len(self.B) - len(self.A)
        self.answer = len(self.A)

    def result(self):
        for i in range(self.sld + 1):
            difference_count = 0
            A_length = len(self.A) + i
            for A, B in zip(self.A, self.B[i:A_length]):
                if A != B:
                    difference_count += 1
            if self.answer > difference_count:
                self.answer = difference_count

        print(self.answer)

if __name__ == '__main__':
    # input = open("./1120.txt")
    P = P1120()
    P.input_data()
    P.result()