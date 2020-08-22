"""
Given a sorted matrix of integers A of size N x M and an integer B.
Each of the rows and columns of matrix A are sorted in ascending order, find the Bth smallest element in the matrix.
NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.
"""
#Incomplete
import heapq
class Maxheap:
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

class Solution:
    def solve(self, A, B):
        heap = Maxheap()
        for i, val in enumerate(A[0]):
            heap.insert((val, (0,i)) )

        for i in range(B):
            print(heap.heap)
            v, i = heap.remove()
            if i[0] < len(A)-1:
                val = A[i[0]+1][i[1]]
                heap.insert((val, (i[0]+1, i[1])))
        return v


t = Solution()
A = [  [5, 9, 11],
        [9, 11, 13],
        [10, 12, 15],
        [13, 14, 16],
        [16, 20, 21] ]
B = 12
print(t.solve(A, B))
                
        

            