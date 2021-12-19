from sys import stdin as input

class P13597:

    def input_data(self):
        self.food_count_list = map(int, input.readline().split())
        self.want_count_list = map(int, input.readline().split())

    def result(self):
        answer = 0
        for f, w in zip(self.food_count_list, self.want_count_list):
            if  (tmp := w - f) > 0:
                answer += tmp
        print(answer)

if __name__ == '__main__':
    # input = open('./15059.txt')
    P = P13597()
    P.input_data()
    P.result()