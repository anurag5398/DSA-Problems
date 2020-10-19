
from collections import defaultdict
class Solution:
    def dfs(self, node, visited, edges):
        visited.add(node)
        if node is None: return 0
        temp = self.B[node]
        for c in edges[node]:
            if c not in visited:
                temp^= self.dfs(c, visited, edges)
        print("node {} xor {}".format(node, temp))
        return temp
            
    
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        self.B = B
        edges = defaultdict(list)
        for s, d in C:
            edges[s].append(d)
            edges[d].append(s)
        visited = set()
        self.maxval, self.maxcount = float('-inf'), 0
        self.dfs(0, visited, edges)
        return []


A = 5
B = [11, 10, 12, 12 , 7]
C = [
    [0,4],
    [1,0],
    [1,3],
    [3,2]
]
t = Solution()
print(t.solve(A, B, C))