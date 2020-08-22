"""
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:
(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.
NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
"""

class Solution:
    #@param A : list of list of int -> 1/0
    #@param i, j : int
    #@param n, m: int
    def fill(self, A, i, j, n, m):
        A[i][j] = 2
        if i - 1 > -1 and A[i - 1][j] == 1:
            self.fill(A, i - 1, j, n, m)
        if i + 1 < n and A[i + 1][j] == 1:
            self.fill(A, i + 1, j, n, m)
        if j + 1 < m and A[i][j + 1] == 1:
            self.fill(A, i, j + 1, n, m)
        if j - 1 > -1 and A[i][j - 1] == 1:
            self.fill(A, i, j - 1, n, m)
        if i - 1 > -1 and j + 1 < m and A[i - 1][j + 1] == 1:
            self.fill(A, i - 1, j + 1, n, m)
        if i + 1 < n and j + 1 < m and A[i + 1][j + 1] == 1:
            self.fill(A, i + 1, j + 1, n, m)
        if i - 1 > -1 and j - 1 > -1 and A[i - 1][j  - 1] == 1:
            self.fill(A, i - 1, j - 1, n, m)
        if i + 1 < n and j - 1 > -1 and A[i + 1][j - 1] == 1:
            self.fill(A, i + 1, j - 1, n, m)

    #@param A : list of list of int -> 1/0
    #@return int -> no of island
    def solve(self, A):
        n, m = len(A), len(A[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    count+=1
                    self.fill(A, i, j, n, m)
        return count

A = [   
       [1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1]    
     ]
t = Solution()
print(t.solve(A))