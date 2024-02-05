from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter


class Heap:
    def __init__(self, arity):
        self.arity = arity
        self.heap = []

    def insert(self, value):
        if value not in self.heap:
            self.heap.append(value)
            self.heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def heapify_up(self, index):
        parent = (index - 1) // self.arity

        if parent < 0:
            return

        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        child = self.get_max_child(index)

        if child is None:
            return

        if self.heap[child] > self.heap[index]:
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            self.heapify_down(child)

    def get_max_child(self, index):
        start = index * self.arity + 1
        end = min(start + self.arity, len(self.heap))

        if start >= len(self.heap):
            return None

        max_index = start
        for i in range(start + 1, end):
            if self.heap[i] > self.heap[max_index]:
                max_index = i

        return max_index

    def display(self):
        """
        Displays the heap as a tree just in terminal.
        """
        if not self.heap:
            print("Heap is empty.")
            return
        print()
        nodes = [Node(str(value)) for value in self.heap]
        for i in range(1, len(nodes)):
            parent_index = (i - 1) // self.arity
            nodes[parent_index].children = nodes[parent_index].children + (nodes[i],)
        root = nodes[0]
        for pre, _, node in RenderTree(root):
            print("%s%s" % (pre, node.name))

    def visualize_tree(self, output_name):
        """
        Visualizes the heap as a tree and saves the output as a picture.

        Args:
        - output_name: a string representing the name of the output file

        Returns:
        - None
        """
        if not self.heap:
            print("Heap is empty.")
            return
        nodes = [Node(str(value)) for value in self.heap]
        for i in range(1, len(nodes)):
            parent_index = (i - 1) // self.arity
            nodes[parent_index].children = nodes[parent_index].children + (nodes[i],)
        root = nodes[0]
        UniqueDotExporter(root).to_picture(output_name)


class BinaryHeap(Heap):
    def __init__(self):
        super().__init__(2)


class FiveHeap(Heap):
    def __init__(self):
        super().__init__(5)


class SevenHeap(Heap):
    def __init__(self):
        super().__init__(7)
