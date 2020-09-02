"""
Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge from i to j (i ---> j).
If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.
Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.
If there is no possible path from vertex i to vertex j , B[i][j] = -1
Note: Rows are numbered from top to bottom and columns are numbered from left to right.
"""
#Floyd warshall suggest to consider each node as intermediate one by one
#TC -> O(v^3) .so sometimes using dijkstra for all node can be better

class Solution:
    #@param A : list of list of int -> edges
    #@return list of list of int -> shortest distance from i to j
    def solve(self, A):
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == -1:
                    A[i][j] = float('inf')

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != k or j != k or i != j:
                        A[i][j] = min(A[i][k] + A[k][j], A[i][j])

        for i in range(n):
            for j in range(n):
                if A[i][j] == float('inf'):
                    A[i][j] = -1
        
        return A



A = [ [0 , 50 , 39],
      [-1 , 0 , 1],
      [-1 , 10 , 0] ]
t = Solution()
print(t.solve(A))