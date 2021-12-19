from sys import stdin as input

class P17099:

    def input_data(self):
        POINT_CNT = 3
        self.A_point = []
        self.B_point = []
        for _ in range(POINT_CNT):
            self.A_point.append(int(input.readline()))
        for _ in range(POINT_CNT):
            self.B_point.append(int(input.readline()))

    def _calculating_score(self):
        point = [3, 2, 1]
        A_sum, B_sum = 0, 0
        for i, (A, B) in enumerate(zip(self.A_point, self.B_point)):
            A_sum += point[i] * A
            B_sum += point[i] * B
        return A_sum, B_sum

    def result(self):
        A_sum, B_sum = self._calculating_score()

        if A_sum > B_sum:
            print("A")
        elif A_sum < B_sum:
            print("B")
        else:
            print("T")


if __name__ == '__main__':
    # input = open('./17099.txt')
    P = P17099()
    P.input_data()
    P.result()