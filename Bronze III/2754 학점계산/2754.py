from sys import stdin as input

class P2754:

    def input_data(self):
        self.point = input.readline()

    def _change_point(self, credit):
        if credit[0] == "A":
            if credit[1] == "+":
                return 4.3
            elif credit[1] == "0":
                return 4.0
            else:
                return 3.7
        elif credit[0] == "B":
            if credit[1] == "+":
                return 3.3
            elif credit[1] == "0":
                return 3.0
            else:
                return 2.7
        elif credit[0] == "C":
            if credit[1] == "+":
                return 2.3
            elif credit[1] == "0":
                return 2.0
            else:
                return 1.7
        elif credit[0] == "D":
            if credit[1] == "+":
                return 1.3
            elif credit[1] == "0":
                return 1.0
            else:
                return 0.7
        elif credit[0] == "F":
            return 0.0

    def result(self):
        print(self._change_point(self.point))


if __name__ == '__main__':
    # input = open('./2754.txt')
    P = P2754()
    P.input_data()
    P.result()