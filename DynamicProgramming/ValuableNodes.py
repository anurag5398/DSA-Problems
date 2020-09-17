"""
Given a tree T containing N nodes numbered [1,2, ..., N] rooted at node 1.
Each node has a value associated with it. You need to choose some of the nodes from the tree such that the sum of values of the chosen nodes is maximum possible.
Moreover, if you have chosen a node V you cannot choose any of its children or grand children.
In simple words, you have to choose a subset of nodes such that no two nodes in the chosen set have a parent-child relation or grandfather-grandchild relation between them.
"""
#Input: First argument is the vector A, where A[i] denotes parent of i+1
#Second argument is the vector B, where B[i] if the value associated with node i+1
from collections import defaultdict, deque
class Solution:
    def dfs(self, node, dp, child, ggc):
        awithout = 0
        for c in child[node]:
            self.dfs(c, dp, child, ggc)
            awithout+= dp[c]
        awith = self.B[node - 1]
        for ccc in ggc[node]:
            awith+= dp[ccc]
        dp[node] = max(awith, awithout)
        
            
    def solve(self, A: list, B: list) -> int:
        self.B = B
        self.ans = float('-inf')
        child, ggc = defaultdict(list), defaultdict(list)
        for node, parent in enumerate(A, 1):
            child[parent].append(node)
            p = parent
            if p != 0:
                gp = A[p - 1]
                if gp != 0:
                    ggp = A[gp - 1]
                    if ggp != 0:
                        ggc[ggp].append(node)

        dp = [0 for _ in range(len(A) + 1)]
        dp[0] = B[0]

        
        self.dfs(1, dp, child, ggc)
        return dp[1]
        
            

A = [0, 1, 1, 2, 2, 4]
B = [5, 7, 9, 4, 6, 8]
t = Solution()
print(t.solve(A, B))