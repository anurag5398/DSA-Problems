"""
You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
Median is the middle element in the sorted list of elements. If the number of elements are even then median will be (sum of both middle elements)/2.
Return 1 if the array is special else return 0.
NOTE:
For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]
"""
#maintain a running median using two heaps

import heapq

class minheap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def insert(self, val):
        self.size+=1
        heapq.heappush(self.heap, val)
    def pop(self):
        self.size-=1
        return heapq.heappop(self.heap)

class maxheap:
    def __init__(self):
        self.heap = []
        self.size = 0
    def insert(self, val):
        self.size+=1
        heapq.heappush(self.heap, -val)
    def pop(self):
        self.size-=1
        return -heapq.heappop(self.heap)

class Solution:
    def findSpecial(self, A):
        minh, maxh = minheap(), maxheap()
        self.median = A[0]
        if A[0] < 0: maxh.insert(A[0])
        else: minh.insert(A[0])
        n = len(A)
        for i in range(1, n):
            if self.median == A[i]: return True

            if A[i] < self.median: maxh.insert(A[i])
            else: minh.insert(A[i])

            if abs(maxh.size - minh.size) >= 2:
                if minh.size > maxh.size:
                    tempval = minh.pop()
                    maxh.insert(tempval)
                else:
                    tempval = maxh.pop()
                    minh.insert(tempval)
            
            if minh.size > maxh.size:
                self.median = minh.heap[0]
            elif maxh.size > minh.size:
                self.median = -maxh.heap[0]
            else:
                self.median = (minh.heap[0] - maxh.heap[0])/2
        return False
            
        

    def solve(self, A):
        if self.findSpecial(A): return 1
        if self.findSpecial(A[-1::-1]): return 1
        return 0 



t = Solution()
A = [770867, 770850, -770262, -770826, 770882, 770552, 770038, -770395, 770509, 770253, -770130, 770966, -770471, -770933, -770002]
print(t.solve(A))
        


        