import sys

# sys.stdin = open('./11279.txt')


class Heap():

    def __init__(self) -> None:
        self.list = [-1]
        self.index = 0

    def empty(self) -> bool:
        if self.index == 0:
            return True
        else:
            return False

    def _swap(self, num1, num2) -> None:
        tmp = self.list[num2]
        self.list[num2] = self.list[num1]
        self.list[num1] = tmp

    def peek(self) -> int:
        if self.empty():
            print(0)
        else:
            print(self.list[1])

    def min_heapify(self, index=1) -> None:
        largest = index

        while largest < self.index:
            left = 2*largest
            right = (2*largest) + 1

            ## 더 작은 수 비교 해서 변경
            if right <= self.index and left <= self.index and \
               self.list[right] > self.list[largest] and \
               self.list[left] > self.list[largest]:
                  if self.list[right] > self.list[left]:
                      self._swap(right, largest)
                      largest = right
                  else:
                      self._swap(left, largest)
                      largest = left
                  continue

            # 오른쪽만 작은경우
            if right <= self.index and \
                    self.list[right] > self.list[largest]:
                self._swap(right, largest)
                largest = right
                continue

            # 왼쪽만 작은경우
            if left <= self.index and \
                    self.list[left] > self.list[largest]:
                 self._swap(left, largest)
                 largest = left
                 continue

            # 중지
            break

    def enqueue(self, num) -> None:
        self.list.append(num)
        self.index += 1
        i = self.index

        while i > 1 and self.list[i//2] < self.list[i]:
            self._swap(i//2, i)
            i //= 2

    def dequeue(self) -> None:
        if self.empty():
            print(0)
            return

        # 루트 노드 맨뒤와 앞 변경
        self._swap(1, self.index)
        print(self.list.pop())
        self.index -= 1

        # 정렬
        self.min_heapify()


H = Heap()
for _ in range(int(sys.stdin.readline())):
    tmp_num = int(sys.stdin.readline())
    if tmp_num == 0:
        H.dequeue()
    else:
        H.enqueue(tmp_num)