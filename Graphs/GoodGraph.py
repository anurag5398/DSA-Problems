"""
Given a directed graph of N nodes where each node is pointing to any one of the N nodes (can possibly point to itself). Ishu, the coder, is bored and he has discovered a problem out of it to keep himself busy. Problem is as follows:
A node is 'good' if it satisfies one of the following:
1. It is the special node (marked as node 1)
2. It is pointing to the special node (node 1)
3. It is pointing to a good node.
Ishu is going to change pointers of some nodes to make them all 'good'. You have to find the minimum number of pointers to change in order to make all the nodes good (Thus, a Good Graph).

NOTE: Resultant Graph should hold the property that all nodes are good and each node must point to exactly one node.
#first find current good nodes, that points to one
#or to someone who points to someone who ...... to one
#then find connected components, other than dfs of 1 (this will be the ans)

"""
from collections import defaultdict

class Solution:
    #@param node : int
    #@param visited : list of bool
    #@param edges : defaultdict
    def dfs(self, node, visited, edges):
        visited[node] = True
        for c in edges[node]:
            if visited[c] is False:
                self.dfs(c, visited, edges)

    #@param A : list of int
    #@return int
    def solve(self, A):
        edges = defaultdict(list)
        fulledges = defaultdict(list)
        for i, v in enumerate(A):
            edges[v].append(i + 1)
            fulledges[v].append(i + 1)
            fulledges[i + 1].append(v)
        
        visited = [False] * (len(A) + 1)
        
        q = [1]
        while q:
            n = q.pop()
            visited[n] = True
            for c in edges[n]:
                if visited[c] is False:
                    q.append(c)
        
        comp = 0
        for i in range(2, len(A) + 1):
            if visited[i] is False:
                comp+=1
                self.dfs(i, visited, fulledges)
        
        return comp

t = Solution()
A = [2, 3, 4, 5, 6, 7, 8, 2]
print(t.solve(A))