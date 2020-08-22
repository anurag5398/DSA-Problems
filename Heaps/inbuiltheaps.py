import heapq
#heapq is minheap
#Functions: heappush, heappop, heapify, heapreplace

class Minheap:
    def __init__(self):
        self.heap = list()
    
    def build(self, array):
        self.heap = array
        heapq.heapify(self.heap)

    def insert(self, val):
        heapq.heappush(self.heap, val)
    
    def remove(self):
        return heapq.heappop(self.heap)

    def replace(self, val):
        return heapq.heapreplace(self.heap, val)

class Maxheap:
    def __init__(self):
        self.heap = list()
    
    def build(self, array):
        self.heap = [-i for i in array]
        heapq.heapify(self.heap)

    def insert(self, val):
        heapq.heappush(self.heap, -val)

    def remove(self):
        return -heapq.heappop(self.heap)
    
    def replace(self, val):
        return -heapq.heapreplace(self.heap, val)


m = Minheap()

m.insert((5, (1,1)))
m.insert((7, (2,2)))
m.insert((2, (7,7)))
m.insert((1, (10, 15)))
#print(m.replace(1))
print(m.heap)