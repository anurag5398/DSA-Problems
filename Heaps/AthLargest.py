"""
Given an integer array B of size N.
You need to find the Ath largest element in the subarray [1 to i] where i varies from 1 to N. In other words, find the Ath largest element in the sub-arrays [1 : 1], [1 : 2], [1 : 3], ...., [1 : N].
NOTE: If any subarray [1 : i] has less than A elements then output array should be -1 at the ith index.
"""
import heapq
class Solution:
    def solve(self, A: int, B: list) -> list:
        n = len(B)
        heap = list()
        ans = [-1 for _ in range(n)]
        if n < A: return ans
        for v in range(A):
            heap.append(B[v])
        heapq.heapify(heap)
        ans[A - 1] = heap[0]

        for i in range(A, n):
            if heap[0] < B[i]:
                heapq.heapreplace(heap, B[i])
            ans[i] = heap[0]
        return ans

t = Solution()
A = 5
B = [1, 2, 3, 4, 5, 6] 
print(t.solve(A, B))
