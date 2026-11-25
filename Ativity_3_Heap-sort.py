class MaxHeap:

    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def extract(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return maximum

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


max_heap = MaxHeap()
numbers = [19, 18, 17, 14, 13, 11, 9, 5]
for number in numbers:
    max_heap.insert(number)

print("Maximum value:", max_heap.peek())
print("Extracted values:")

while max_heap.size() > 0:
    print(max_heap.extract(), end=" ")

print("\n")


def heap_sort(array):
    max_heap = MaxHeap()

    for number in array:
        max_heap.insert(number)

    result = []

    while max_heap.size() > 0:
        result.insert(0, max_heap.extract())

    return result


print(heap_sort([4, 10, 3, 5, 1]))
print(heap_sort([1, 2, 3, 4, 5]))
print(heap_sort([5, 4, 3, 2, 1]))
print(heap_sort([4, 2, 4, 1, 2]))
print(heap_sort([]))

print()