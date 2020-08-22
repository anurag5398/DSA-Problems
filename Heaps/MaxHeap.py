import math
class Maxheap:
    def __init__(self):
        self.tree = []
        self.size = -1
    
    def swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]

    def upheapify(self, index):
        parent = (index-1)//2
        while parent >= 0:
            if self.tree[parent] < self.tree[index]:
                self.swap(parent, index)
            index = parent
            parent = (index-1)//2

    def insert(self, val):
        self.tree.append(val)
        self.size+=1
        self.upheapify(self.size)

    def maxchild(self, index):
        if 2 * index + 2 > self.size:
            return 2*index+1
        else:
            if self.tree[2*index+1] >= self.tree[2*index+2]:
                return 2*index+1
            else:
                return 2*index+2

    def downheapify(self, index):
        while 2 * index + 1 <= self.size:
            mc = self.maxchild(index)
            if self.tree[mc] > self.tree[index]:
                self.swap(mc, index)
            index = mc

    def delete(self):
        if self.size < 0: return None
        if self.size == 0:
            self.size-=1
            return self.tree.pop()
        
        val = self.tree[0]
        self.swap(0, self.size)
        self.tree.pop()
        self.size-=1
        self.downheapify(0)
        return val

    def build(self, array):
        self.tree = self.tree + array
        self.size = self.size + len(array)
        leaves = math.ceil((self.size+1)/2)
        index = self.size - leaves
        while index >= 0:
            self.downheapify(index)
            index-=1

mh = Maxheap()
mh.build([5,7,3,2,10])
print(mh.tree)

#print(mh.delete())
#print(mh.tree)

mh.insert(5)
print(mh.tree)

mh.insert(5)
print(mh.tree)


