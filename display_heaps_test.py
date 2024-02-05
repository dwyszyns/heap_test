from heaps import Heap
import random


def display_heaps_test(heap_size, arity):
    random_list = [random.randint(1, 1000) for _ in range(10000)]
    random_list = set(random_list)
    list_rand = list(random_list)
    input_list = list_rand[1:heap_size]
    heap = Heap(arity)
    for x in input_list:
        heap.insert(x)
  
    heap.visualize_tree(f"Output-{arity}.png")
    heap.delete()
    heap.visualize_tree(f"Output2-{arity}.png")



if __name__ == '__main__':
    display_heaps_test(64, 2)
    display_heaps_test(31, 5)
    display_heaps_test(57, 7)
