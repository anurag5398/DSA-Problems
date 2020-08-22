"""
Given an array of integers A and an integer B. You must modify the array exactly B number of times. In single modification, we can replace any one array element A[i] by -A[i].
You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.
"""

from heapq import heapify, heappop, heappush
class Solution:
    def solve(self, A, B):
        heapify(A)
        for i in range(B):
            x = heappop(A)
            heappush(A, -x)
        return sum(A)

t = Solution()
A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
B = 10
print(t.solve(A, B))
