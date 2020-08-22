"""
We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0).
Here, the distance between two points on a plane is the Euclidean distance.
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)
NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).
"""

import heapq
import math
class Maxheap:
    def __init__(self):
        self.heap = list()
    
    def build(self, array):
        self.heap = [-i for i in array]
        heapq.heapify(self.heap)

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def remove(self):
        return heapq.heappop(self.heap)
    
    def replace(self, val):
        return heapq.heapreplace(self.heap, val)


class Solution:
    def distance(self, point):
        return math.sqrt(point[0]**2+point[1]**2)

    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        heap = Maxheap()
        for index, val in enumerate(A):
            temp = (-self.distance(val), val)
            if index < B:
                heap.insert(temp)
            else:
                if temp[0] > heap.heap[0][0]:
                    heap.replace(temp)
        return [i for v, i in heap.heap]

t= Solution()
A = [
       [1, -1],
       [2, -1]
     ] 
B = 1
print(t.solve(A, B))
