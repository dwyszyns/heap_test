import unittest
import matplotlib.pyplot as plt
from heaps import Heap
from time import time
import mplcursors


class TestHeap(unittest.TestCase):
    def test_empty_list(self):
        heap2 = Heap(2)
        self.assertEqual(heap2.heap, [])

    def test_remove_from_empty_list(self):
        heap2 = Heap(2)
        heap2.delete()
        self.assertEqual(heap2.heap, [])

    def test_insert_value(self):
        heap2 = Heap(2)
        heap2.insert(2)
        self.assertEqual(heap2.heap, [2])

    def test_insert_delete_value(self):
        heap2 = Heap(2)
        heap2.insert(2)
        heap2.insert(0)
        heap2.delete()
        self.assertEqual(heap2.heap, [0])

    def test_insert(self):
        heap = Heap(2)
        heap.insert(5)
        heap.insert(3)
        heap.insert(7)
        heap.insert(1)
        heap.insert(9)
        heap.insert(2)
        heap.insert(10)
        heap.insert(90)
        heap.insert(70)
        heap.insert(50)
        heap.insert(23)
        heap.insert(45)
        heap.insert(33)
        heap.insert(11)
        heap.display()
        self.assertEqual(heap.heap, [90, 70, 45, 10, 50, 33, 11, 1, 7, 3, 23, 2, 9, 5])

    def test_delete(self):
        heap = Heap(2)
        heap.heap = [9, 7, 2, 1, 5, 3]
        heap.display()
        self.assertEqual(heap.delete(), 9)
        heap.display()
        self.assertEqual(heap.heap, [7, 5, 2, 1, 3])
        self.assertEqual(heap.delete(), 7)
        heap.display()
        self.assertEqual(heap.heap, [5, 3, 2, 1])
        self.assertEqual(heap.delete(), 5)
        self.assertEqual(heap.heap, [3, 1, 2])
        heap.display()
        self.assertEqual(heap.delete(), 3)
        self.assertEqual(heap.heap, [2, 1])
        self.assertEqual(heap.delete(), 2)
        heap.display()
        self.assertEqual(heap.heap, [1])
        self.assertEqual(heap.delete(), 1)
        self.assertEqual(heap.heap, [])
        self.assertEqual(heap.delete(), None)

    def test_display(self):
        heap = Heap(2)
        heap.insert(9)
        heap.insert(7)
        heap.insert(2)
        heap.insert(1)
        heap.insert(5)
        heap.insert(3)
        heap.insert(8)
        heap.insert(11)
        heap.insert(13)
        heap.insert(41)
        heap.insert(55)
        heap.insert(33)
        heap.insert(55)
        heap.insert(33)
        heap.insert(75)
        heap.insert(63)
        heap.insert(45)
        heap.insert(13)
        heap.display()
        heap.visualize_tree("test_display.png")

    def test_heap_creation_time(self):
        with open("random_numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f]
            input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
            heap_types = [Heap(2), Heap(5), Heap(6), Heap(7), Heap(8), Heap(9), Heap(10), Heap(100)]
            times = [[] for _ in range(len(heap_types))]

            for size in input_sizes:
                input_list = numbers[1:size]
                for i, heap_type in enumerate(heap_types):
                    time_start = time()
                    heap = Heap(heap_type.arity)
                    for x in input_list:
                        heap.insert(x)
                    time_end = time()
                    times[i].append(time_end-time_start)

            plt.plot(input_sizes, times[0], label="Arity 2")
            plt.plot(input_sizes, times[1], label="Arity 5")
            plt.plot(input_sizes, times[2], label="Arity 6")
            plt.plot(input_sizes, times[2], label="Arity 7")
            plt.plot(input_sizes, times[3], label="Arity 8")
            plt.plot(input_sizes, times[4], label="Arity 9")
            plt.plot(input_sizes, times[5], label="Arity 10")
            plt.plot(input_sizes, times[6], label="Arity 100")
            mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()}: {sel.target[1]:.6f} s'))
            plt.xlabel("Input size")
            plt.ylabel("Time (s)")
            plt.title("Heap creation time")
            plt.legend()
            plt.savefig("heaps_plot_creation_time.png")
            plt.show()

    def test_heap_deletion_time(self):
        with open("random_numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f]
            input_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
            heap_types = [Heap(2), Heap(5), Heap(6), Heap(7), Heap(8), Heap(9), Heap(10), Heap(100)]
            times = [[] for _ in range(len(heap_types))]
            for size in input_sizes:
                input_list = numbers[1:size]
                for i, heap_type in enumerate(heap_types):
                    heap = Heap(heap_type.arity)
                    for x in input_list:
                        heap.insert(x)
                    time_start = time()
                    for x in heap.heap:
                        heap.delete()
                    time_end = time()
                    times[i].append(time_end-time_start)
        plt.plot(input_sizes, times[0], label="Arity 2")
        plt.plot(input_sizes, times[1], label="Arity 5")
        plt.plot(input_sizes, times[2], label="Arity 6")
        plt.plot(input_sizes, times[2], label="Arity 7")
        plt.plot(input_sizes, times[3], label="Arity 8")
        plt.plot(input_sizes, times[4], label="Arity 9")
        plt.plot(input_sizes, times[5], label="Arity 10")
        plt.plot(input_sizes, times[6], label="Arity 100")
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f'{sel.artist.get_label()}: {sel.target[1]:.6f} s'))
        plt.xlabel("Input size")
        plt.ylabel("Time (s)")
        plt.title("Heap deletion time")
        plt.legend()
        plt.savefig("heaps_plot_deletion_time.png")
        plt.show()


if __name__ == '__main__':
    unittest.main()
