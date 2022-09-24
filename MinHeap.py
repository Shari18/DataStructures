class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        raise Exception("Heap is empty")

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _rise(self, index):
        parent_index = self._parent(index)
        while index >= 0 and parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            # swap
            self.heap[parent_index], self.heap[index] = (
                self.heap[index],
                self.heap[parent_index],
            )
            index = parent_index
            parent_index = self._parent(index)

    def push(self, x):
        self.heap.append(x)
        self._rise(len(self.heap) - 1)

    def _sink(self, index):
        while True:
            left_child_index = self._left_child(index)
            if left_child_index >= len(self.heap):
                break
            child_index = left_child_index
            right_child_index = self._right_child(index)
            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] < self.heap[left_child_index]
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
        self.heap[0], self.heap[-1] = (
            self.heap[-1],
            self.heap[0],
        )
        x = self.heap.pop()
        self._sink(0)
        return x

    def build_heap_from_random_arr(self, arr):
        self.heap = arr
        for i in range((len(arr) // 2) - 1, -1, -1):
            self._sink(i)
