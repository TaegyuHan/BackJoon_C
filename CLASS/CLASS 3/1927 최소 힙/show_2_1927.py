import sys
input = sys.stdin.readline

class minHeap():
	def __init__(self, max_size):
		self.heap = [None] * max_size
		self.heap_size = 0

	def is_empty(self):
		if self.heap_size == 0:
			return True
		else:
			return False

	def insert(self, item):
		self.heap_size += 1
		i = self.heap_size

		while i != 1 and self.heap[i//2] > item:
			self.heap[i] = self.heap[i//2]
			i = i//2

		self.heap[i] = item

	def delete(self):
		if self.is_empty():
			return 0
		else:
			item = self.heap[1]
			temp = self.heap[self.heap_size]
			self.heap_size -= 1

			parent = 1
			child = 2

			while child <= self.heap_size:
				if child < self.heap_size and self.heap[child] > self.heap[child+1]:
					child += 1

				if self.heap[child] > temp:
					break
		 	
				self.heap[parent] = self.heap[child]
				parent = child
				child *= 2

			self.heap[parent] = temp
			return item

if __name__ == "__main__":
	minH = minHeap(100000)
	result = []

	N = int(input().strip())
	
	for _ in range(0, N):
		tmp = int(input().strip())
		if tmp == 0:
			result.append(minH.delete())
		else:
			minH.insert(tmp)

	for i in result:
		print(i)