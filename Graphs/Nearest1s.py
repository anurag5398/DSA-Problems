"""
Given a matrix of integers A of size N x M consisting of 0 or 1.
For each cell of the matrix find the distance of nearest 1 in the matrix.
Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.
Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.
NOTE: There is atleast one 1 is present in the matrix.
"""
#From each 1 perform bfs, and increase distance in all 4 directions
from collections import deque
class Solution:
    #@param i, j : int
    #@return bool
    def isbound(self, i, j):
        if i < 0 or i >= self.n: return False
        if j < 0 or j >= self.m: return False
        return True
    #param A : list of list of int
    #@return list of list of int
    def solve(self, A):
        ans = [[-1 for _ in range(len(A[0]))] for _ in range(len(A))]
        self.n, self.m = len(A), len(A[0])
        q = deque()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    ans[i][j] = 0
                    q.append((0, i, j))
        
        change_i = [-1, 0, 1, 0]
        change_j = [0, 1, 0, -1]
        while q:
            d, i, j = q.popleft()
            for ci, cj in zip(change_i, change_j):
                if self.isbound(i + ci, j + cj) and ans[i + ci][j + cj] == -1:
                    ans[i + ci][j + cj] = d + 1
                    q.append((d + 1, i + ci, j + cj))
        return ans

A = [
       [0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 1, 1, 0],
     ]

t = Solution()
print(t.solve(A))
            

