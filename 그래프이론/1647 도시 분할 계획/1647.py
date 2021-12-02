from sys import stdin as input

class P1647:
    def __init__(self):
        self.city_cnt = 0
        self.load_cnt = 0
        self.city_list = []
        self.load_list = []
        self.answer = 0

    def input_data(self):
        self.city_cnt, self.load_cnt = \
            map(int, input.readline().split())

        for i in range(self.city_cnt + 1):
            self.city_list.append(i)

        for _ in range(self.load_cnt):
            self.load_list.append(tuple(map(int, input.readline().split())))
            self.load_list.sort(key=lambda x:x[2])

    def _find_root_city(self, city):
        if self.city_list[city] != city:
            self.city_list[city] = self._find_root_city(self.city_list[city])
        return self.city_list[city]

    def _find_load(self):
        i = 1
        for city1, city2, cost in self.load_list:
            root_city1 = self._find_root_city(city1)
            root_city2 = self._find_root_city(city2)

            if root_city1 == root_city2:
                continue

            if root_city1 < root_city2:
                self.city_list[root_city2] = root_city1
            else:
                self.city_list[root_city1] = root_city2

            if i >= self.city_cnt - 1:
                break

            self.answer += cost
            i += 1

    def result(self):
        self._find_load()
        print(self.answer)


if __name__ == "__main__":
    # input = open("./1647.txt")
    P = P1647()
    P.input_data()
    P.result()
