import sys

sys.stdin = open('./1927.txt')

count = int(sys.stdin.readline())

class Heap():

    def __init__(self) -> None:
        self.data_list = [0]
        self.index = 0
  
    def _swap(self, num1, num2) -> None:
        tmp = self.data_list[num2]
        self.data_list[num2] = self.data_list[num1]
        self.data_list[num1] = tmp

    def _check_empty(self) -> bool:
        if self.index == 0:
            return True
        else:
            return False

    def _up_sort(self) -> None:
        a_index = self.index
        while a_index > 1:
            b_index = a_index//2

            if self.data_list[a_index] <= self.data_list[b_index]:
                self._swap(a_index, b_index)
                a_index = b_index
            else: 
              break

    def _down_sort(self) -> None:
        a_index = 1
        while a_index <= self.index:
            # print(a_index)
            if (b_index := a_index*2) < self.index:
                if self.data_list[a_index] >= self.data_list[b_index]:
                    self._swap(a_index, b_index)
                    a_index = b_index

            if (b_index := a_index*2 + 1) < self.index:
                if self.data_list[a_index] >= self.data_list[b_index]:
                    self._swap(a_index, b_index)
                    a_index = b_index

            a_index = b_index

            # print(self.data_list)

    def enqueue(self, data: int) -> None:
        self.data_list.append(data)
        self.index += 1
        self._up_sort()

    def dequeue(self) -> None:
        if self._check_empty():
            print(0)
            return
        else:
            tmp = self.data_list[1]
            self.data_list[1] = self.data_list[self.index]
            self.data_list[self.index] = tmp
            print(self.data_list.pop())
            self.index -= 1
            p._down_sort()

p = Heap()
for _ in range(count):
    print(p.data_list)
    if (input := int(sys.stdin.readline())) == 0:
        p.dequeue()
    else:
        p.enqueue(input)