import sys

sys.stdin = open('./1927.txt')

input_data_count = int(sys.stdin.readline())

class Heap():

  def __init__(self):
      self.list = [0]
      self.data_index = 0
      self.len = 0

  def show_list(self):
      print(self.list)

  def check_empty(self):
      if self.data_index == 0 and self.len == 0:
        return True
      else:
        return False

  def compare_list(self):
      index_a = self.data_index
      index_b = self.data_index // 2
      print(index_a,index_b)

  def in_data(self, data):
      self.list.append(data)
      self.data_index += 1
      self.len += 1

      if self.len > 1:
        self.compare_list()
  
  def out_data(self):
      if self.check_empty() == True:
          print(0)
          return

      print(self.list[self.data_index-1])
      self.list[0] = self.list[self.data_index-1]
      self.data_index -= 1
      self.len -= 1


if __name__ == '__main__':
    heap = Heap()
    heap.in_data(5)
    heap.in_data(4)
    heap.in_data(3)
    heap.in_data(2)
    heap.in_data(1)
    heap.show_list()
    heap.out_data()

