from sys import stdin as input


class P14935:

    def input_data(self):
        self.x = input.readline()
        self.back = self.x
        self.next = self.x

    def result(self):
        not_nfa = True
        while True:
            self.next = str(int(self.next[0]) * len(self.next))
            if self.back == self.next:
                print("FA")
                not_nfa = True
                break
            self.back = self.next

        if not not_nfa:
            print("NFA")


if __name__ == '__main__':
    # input = open('./14935.txt')
    P = P14935()
    P.input_data()
    P.result()