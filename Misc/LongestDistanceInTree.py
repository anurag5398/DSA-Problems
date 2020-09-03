"""
Find largest distance Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes.
The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).
The nodes will be numbered 0 through N - 1.
The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.
"""
from collections import defaultdict
class Solution:
    #@param root : int
    #@param edges : defaultdict
    #@return int
    def distance(self, root, edges):
        if root is None: return 0
        tempmax = 0
        for c in edges[root]:
            temp = self.distance(c, edges)
            self.ans = max(temp + tempmax, self.ans)
            tempmax = max(temp, tempmax)
        return tempmax + 1


    #@param A : list of int
    #@return int
    def solve(self, A):
        edges = defaultdict(list)
        root = -1
        for i, v in enumerate(A):
            if v == -1:
                root = i
                continue
            edges[v].append(i)
        #print(edges)
        self.ans = 0
        self.distance(root, edges)
        return self.ans





A = [-1]
t = Solution()
print(t.solve(A))