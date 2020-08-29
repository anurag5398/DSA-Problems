"""
You are given an undirected unweighted graph consisting of A vertices and M edges given in a form of 2D Matrix B of size M x 2 where (B[i][0], B][i][1]) denotes two nodes connected by an edge.
You have to write a number on each vertex of the graph. Each number should be 1, 2 or 3. The graph becomes Poisonous if for each edge the sum of numbers on vertices connected by this edge is odd.
Calculate the number of possible ways to write numbers 1, 2 or 3 on vertices so the graph becomes poisonous. Since this number may be large, return it modulo 998244353.
NOTE:
Note that you have to write exactly one number on each vertex.
The graph does not have any self-loops or multiple edges.
Nodes are labelled from 1 to A.
"""
import collections
class Solution:
    def dfs(self, node, color, edges):
        if self.loop: return
        for c in edges[node]:
            if color[c] == -1:
                color[c] = color[node]^1
                self.count[color[c]]+=1
                self.dfs(c, color, edges)
            elif color[c] == color[node]:
                self.loop = True


    def solve(self, A, B):
        edges = collections.defaultdict(list)
        for s, d in B:
            edges[s].append(d)
            edges[d].append(s)
        
        ans = 1
        self.loop = False
        color = [-1 for _ in range(A + 1)]
        for i in range(1, A + 1):
            if color[i] == -1:
                self.count = [1, 0]
                color[i] = 0
                self.dfs(i, color, edges)
                if self.count == [1, 0]:
                    temp = 3
                    ans = (ans * temp)%998244353
                else:
                    temp = (2**self.count[0])%998244353 + (2**self.count[1])%998244353
                    ans = (ans * temp)%998244353
        if self.loop: return 0
        return ans%998244353
                

A = 4
B = [
  [1, 2],
  [1, 3],
  [1, 4],
  [2, 3],
  [2, 4],
  [3, 4]
]
t = Solution()
print(t.solve(A, B))