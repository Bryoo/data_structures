
class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, element):
        self.heap_list.append(element)
        self.current_size = self.current_size + 1
        self.insertion_heapify(self, self.current_size)

    def insertion_heapify(self, pos):
        while pos // 2 > 0:
            if self.heap_list[pos] > self.heap_list[pos//2]:
                self.heap_list[pos], self.heap_list[pos//2] = self.heap_list[pos//2],  self.heap_list[pos]
            pos = pos // 2

    def delete_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.down_heapify(1)
        return retval
    
    def down_heapify(self, pos):
        while (pos * 2) <= self.current_size:
            mc = self.min_child(pos)
            if self.heap_list[pos] > self.heap_list[mc]:
                tmp = self.heap_list[pos]
                self.heap_list[pos] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            pos = mc

    def min_child(self, pos):
        if pos * 2 + 1 > self.current_size:
            return pos * 2
        else:
            if self.heap_list[pos * 2] < self.heap_list[pos * 2 + 1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def build_heap(self, alist):
        pos = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (pos > 0):
            self.down_heapify(pos)
            pos = pos - 1

bh = BinHeap()
bh.build_heap([9,5,6,2,3])

print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
