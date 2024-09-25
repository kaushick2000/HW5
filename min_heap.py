class min_heap:
    def __init__(self, data=None):
        self.heap = data if data else []
        if self.heap:
            self.build_min_heap()

    def parent(self, i):

        return (i - 1) >> 1

    def left(self, i):

        return (i << 1) + 1

    def right(self, i):

        return (i << 1) + 2

    def build_min_heap(self):

        for i in range(self.parent(len(self.heap) - 1), -1, -1):
            self.heapify_down(i)

    def heapify_down(self, i):

        n = len(self.heap)
        smallest = i
        left_child = self.left(i)
        right_child = self.right(i)


        if left_child < n and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < n and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child


        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def heapify_up(self, i):

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with the parent and move up
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, key):

        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):

        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        root = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.heapify_down(0)

        return root

    def peek(self):

        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def __str__(self):

        return str(self.heap)



if __name__ == "__main__":
    data = [12, 3, 10, 1, 8, 5]
    # using float values
    # data1=[12.3,3.5,10.4,1.7,8.2,5.6]
    heap = min_heap(data)
    print("Initial Min Heap:", heap)

    print("\nInserting element 3 into the Min Heap:")
    heap.insert(3)
    print("Min Heap after insertion:", heap)

    print("\nPopping the root element (min) from the Min Heap:")
    root = heap.pop()
    print("Popped element:", root)
    print("Min Heap after popping the root:", heap)

    print("\nPeeking the root element (min) without removing:")
    root_peek = heap.peek()
    print("Peeked element:", root_peek)
    print("Min Heap after peeking (no change):", heap)
