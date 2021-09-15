from sys import stdin

class PROBLEM_2018():

    def __init__(self):
        self.data_count = 0
        self.data_list = []
        self.sum = 0
        self.mode = 0

    def quick_sort(self, arr):

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        lesser_arr, equal_arr, greater_arr = [], [], []

        for num in arr:
            if num < pivot:
                lesser_arr.append(num)
            elif num > pivot:
                greater_arr.append(num)
            else:
                equal_arr.append(num)

        return self.quick_sort(lesser_arr) + equal_arr + self.quick_sort(greater_arr)

    def input_data(self):
        data = stdin.readline()
        return data;

    def scan_loop(self):

        # 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)
        self.data_count = int(self.input_data())

        # 다음 N개의 줄에는 정수들이 주어진다. 
        # 정수의 절댓값은 4,000을 넘지 않는다.
        for _ in range(self.data_count):
            self.temp_int = int(self.input_data())

            # 리스트에 데이터 넣기
            self.data_list.append(self.temp_int)

            # 합
            self.sum += self.temp_int
        
        # 데이터 정렬
        self.data_list = self.quick_sort(self.data_list)

    # 평균
    def mean(self):
        print(round(self.sum / self.data_count))

    # 중앙값
    def median(self):
        print(self.data_list[round(self.data_count / 2)])


    def _range(self):
        print(self.data_list[self.data_count-1] - self.data_list[0])


if __name__ == '__main__':
    a = PROBLEM_2018()

    a.scan_loop()
    # a.mean()
    # a.median()
    a._mode()
    # a._range()