"""
Given a tree with N nodes labeled from 1 to N.
Each node has a certain weight assigned to it given by an integer array A of size N.
Your task is to find the maximum difference in weights of two nodes where one node is a descendant of the other.
NOTE:
The tree is rooted at node labeled with 1.
"""
from collections import defaultdict
class Solution:
    #@param node : int
    #@param edges : defaultdict 
    def dfs(self, node: int, edges: defaultdict):
        if not edges[node]: return self.A[node - 1], self.A[node - 1]
        tempmax, tempmin = float('-inf'), float('inf')
        for c in edges[node]:
            mi, ma = self.dfs(c, edges)
            self.maxdiff = max(abs(self.A[node - 1] - mi), abs(self.A[node - 1] - ma), self.maxdiff )
            tempmin = min(mi, self.A[node - 1], tempmin)
            tempmax = max(ma, self.A[node - 1], tempmax)
        return tempmin, tempmax
        

    #@param A : list of int
    #@param B : list of list of int
    #@return int
    def solve(self, A: list, B: list) -> int:
        if len(A) < 2: return 0
        self.A = A
        flag = None
        for s, d in B:
            if s == 1:
                flag = True
                break
            elif d == 1:
                flag = False
                break

        edges = defaultdict(list)
        if flag is True:
            for s, d in B:
                edges[s].append(d)
        else:
            for s, d in B:
                edges[d].append(s)
        
        self.maxdiff = float('-inf')
        self.dfs(1, edges)
        return self.maxdiff

t = Solution()
A = [ -38, 57, -63, -41, 23 ]
B = [
  [1, 2],
  [1, 3],
  [2, 4],
  [2, 5]
]
print(t.solve(A, B))