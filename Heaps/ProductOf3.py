"""
Given an integer array A of size N.
You have to find the product of the 3 largest integers in array A from range 1 to i, where i goes from 1 to N.
Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A. If i < 3, then the integer at index i is -1.
"""

from heapq import heapify, heappop, heappush
class Solution:
    def solve(self, A):
        if len(A) == 0: return []
        if len(A) == 1: return [-1]
        if len(A) == 2: return [-1, -1]

        running = A[0:3]
        tempans = 1
        for val in running: tempans*= val
        ans = [-1,-1,tempans]

        heapify(running)

        for i in range(3, len(A)):
            if running[0] < A[i]:
                smallest = heappop(running)
                tempans = (tempans*A[i])//smallest
                heappush(running, A[i])
            ans.append(tempans)
        return ans

t = Solution()
A = [10, 2, 13, 4]
print(t.solve(A))

        