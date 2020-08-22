"""
Given an array of integers A representing the length of ropes.
You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths.
Find and return the minimum cost to connect these ropes into one rope.
"""

import heapq

class Solution:
    def solve(self, heap):
        heapq.heapify(heap)
        ans = 0
        while len(heap) > 1:
            one = heapq.heappop(heap)
            two = heapq.heappop(heap)
            temp = one+two
            ans+= temp
            heapq.heappush(heap, temp)
        return ans

t = Solution()
A = [5, 17, 100, 11]
print(t.solve(A))
