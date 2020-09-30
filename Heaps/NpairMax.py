"""
Given two integers arrays A and B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.
"""
import heapq
class Solution:
    #@param A: list of int
    #@param B: list of int
    #@return list of int
    def solve(self, A: list, B: list) -> list:
        N = len(A)
        A, B = sorted(A, reverse = True), sorted(B, reverse = True)
        heap = [(-A[0] - B[0], 0, 0)]
        ans = list()
        used = set()
        for _ in range(N):
            val, i, j = heapq.heappop(heap)
            ans.append(-val)
            if i + 1 < N and (i + 1, j) not in used:
                heapq.heappush(heap, (-A[i + 1] - B[j], i + 1, j))
                used.add((i + 1, j))
            if j + 1 < N and (i, j + 1) not in used:
                heapq.heappush(heap, (-A[i] - B[j + 1], i, j + 1))
                used.add((i, j + 1))
        return ans
t = Solution()
A = [2, 4, 1, 1]
B = [-2, -3, 2, 4]
print(t.solve(A, B))

