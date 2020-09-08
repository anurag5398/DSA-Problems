"""
Given three prime number(A, B, C) and an integer D. Find the first(smallest) D integers which have only A, B, C or a combination of them as their prime factors.
"""

#initially start with A, B, C in heap, take out minimum and insert its multiples

from heapq import heapify, heappush, heappop
class Solution:
    #@param A, B, C : int
    #@param D : int
    #@return list of int
    def solve(self, A, B, C, D):
        heap = [A, B, C]
        ans = list()
        heapify(heap)
        i = 0
        while i < D:
            number = heappop(heap)
            if i == 0 or ans[-1] != number:
                ans.append(number)
                i+=1
                heappush(heap, A * number)
                heappush(heap, B * number)
                heappush(heap, C * number)
        return ans




t = Solution()
A, B, C = 2, 3, 5
D = 5
print(t.solve(A, B, C, D))