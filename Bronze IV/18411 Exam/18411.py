from sys import stdin as input

class P18411:

    def input_data(self):
        self.test_scores_list = list(map(int, input.readline().split()))

    def result(self):
        sum_scores = sum(self.test_scores_list)
        min_scores = min(self.test_scores_list)
        print(sum_scores - min_scores)

if __name__ == '__main__':
    # input = open('./18411.txt')
    P = P18411()
    P.input_data()
    P.result()