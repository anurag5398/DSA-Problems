"""
Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

class Solution:
    #@param A: list of str
    #@param ogival: str
    #@param newval: str
    def replace(self, A: list, ogival: str, newval: str) -> None:
        for i in range(self.n):
            for j in range(self.m):
                if A[i][j] == ogival:
                    A[i][j] = newval

    #@param i: int
    #@param j: int
    #@return bool
    def inbounds(self, i: int, j: int) -> bool:
        if i < 0 or i >= self.n: return False
        if j < 0 or j >= self.m: return False
        return True

    #@param A: list of str
    #@param i: int
    #@pram j: int
    def dfs(self, A: list, i: int, j: int) -> None:
        A[i][j] = 'O'
        i_change = [-1, 0, 1, 0]
        j_change = [0, 1, 0, -1]
        for ic, jc in zip(i_change, j_change):
            if self.inbounds(i + ic, j + jc) and A[i + ic][j + jc] == 'Z':
                self.dfs(A, i + ic, j + jc)

    #@param A: list of str
    #@return list of str
    def solve(self, A: list) -> list:
        self.n, self.m = len(A), len(A[0])
        for i in range(self.n):
            A[i] = list(A[i])
        self.replace(A, 'O', 'Z')
        
        for j in range(self.m):
            if A[0][j] == 'Z':
                self.dfs(A, 0, j)
            if A[self.n - 1][j] == 'Z':
                self.dfs(A, self.n - 1, j)
        
        for i in range(self.n):
            if A[i][0] == 'Z':
                self.dfs(A, i, 0)
            if A[i][self.m - 1] == 'Z':
                self.dfs(A, i, self.m - 1)
        
        self.replace(A, 'Z', 'X')

        for i in range(self.n):
            A[i] = "".join(A[i])
        return A



A = ["XXX","XOX","XXX"]
t = Solution()
print(t.solve(A))