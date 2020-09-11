"""
Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add original value(value stored at index before we did any operations) to it's current value. You can choose any of the N elements in each operation.
Perform B operations in such a way that the largest element of the modified array(after B operations) is minimised. Find the minimum possible largest element after B operations.
"""
#store (next_values,  original_value)

import heapq
class Solution:
    #@param A : list of int
    #@param B : int
    #@return int
    def solve(self, A: list, B: int) -> int:
        heap = list()
        maxval = float('-inf')
        for value in A:
            heap.append((2 * value, value))
            maxval = max(value, maxval)
        heapq.heapify(heap)

        for _ in range(B):
            next, multip = heapq.heappop(heap)
            maxval = max(next, maxval)
            heapq.heappush(heap, (next + multip, multip))
        
        return maxval

t = Solution()
A = [5, 1, 4, 2] 
B = 5
print(t.solve(A, B))
