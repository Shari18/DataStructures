class MinHeap:
    def __init__(self):
        self.heap = []

    def get_size(self):
        return len(self.heap)

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        raise Exception("Heap is empty")

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def rise(self, index):
        parent_index = self.parent(index)
        while index >= 0 and parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            # swap
            self.heap[parent_index], self.heap[index] = (
                self.heap[index],
                self.heap[parent_index],
            )
            index = parent_index
            parent_index = self.parent(index)

    def push(self, x):
        self.heap.append(x)
        self.rise(len(self.heap) - 1)

    def sink(self, index):
        while True:
            child_index = self.left_child(index)
            if child_index >= len(self.heap):
                break
            right_child_index = self.right_child(index)
            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] < self.heap[child_index]
            ):
                child_index = right_child_index
            if self.heap[index] > self.heap[child_index]:
                # swap
                self.heap[index], self.heap[child_index] = (
                    self.heap[child_index],
                    self.heap[index],
                )
                index = child_index
            else:
                break

    def pop(self):
        """
        pops first item of heap, which is the min element
        :return:
        """
        # swap last and first item
        self.heap[0], self.heap[len(self.heap) - 1] = (
            self.heap[len(self.heap) - 1],
            self.heap[0],
        )
        x = self.heap.pop()
        self.sink(0)
        return x

    def build_heap_from_random_arr(self, arr):
        self.heap = arr
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.sink(i)
