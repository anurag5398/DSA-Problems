"""
A sorted array of integers, A contains 1, plus some number of primes. Then, for every p < q in the list, we consider the fraction p/q.
What is the B-th smallest fraction considered?
Return your answer as an array of integers, where answer[0] = p and answer[1] = q.
"""
import heapq

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
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        heap = Maxheap()
        count = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                temp = A[i]/A[j]
                print(temp, heap.heap)
                if count < B:
                    heap.insert((-temp, (A[i], A[j] )))
                    count+=1
                else:
                    if -heap.heap[0][0] > temp:
                        heap.replace((-temp, (A[i], A[j])))
        return (heap.heap[0][1])

t = Solution()
A = [1, 7]
B = 1
t.solve(A, B)