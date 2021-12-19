from sys import stdin as input

class P20839:

    def input_data(self):
        subject = ['A', 'C', 'E']
        self.goal_score = {}
        self.my_score = {}

        for sb, point in zip(subject, map(int, input.readline().split())):
            self.goal_score[sb] = point

        for sb, point in zip(subject, map(int, input.readline().split())):
            self.my_score[sb] = point

    def result(self):
        if self.my_score['A'] >= self.goal_score['A'] and \
                self.my_score['C'] >= self.goal_score['C'] and \
                self.my_score['E'] >= self.goal_score['E']:
            print('A')

        elif self.my_score['A'] >= self.goal_score['A'] / 2 and \
                self.my_score['C'] >= self.goal_score['C'] and \
                self.my_score['E'] >= self.goal_score['E']:
            print('B')

        elif self.my_score['C'] >= self.goal_score['C'] and \
                self.my_score['E'] >= self.goal_score['E']:
            print('C')

        elif self.my_score['C'] >= self.goal_score['C'] / 2 and \
                self.my_score['E'] >= self.goal_score['E'] / 2:
            print('D')
        else:
            print('E')


if __name__ == '__main__':
    # input = open('./20839.txt')
    P = P20839()
    P.input_data()
    P.result()