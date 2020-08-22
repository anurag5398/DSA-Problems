"""
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node
B[i][0] to node B[i][1].
Find whether a path exists from node 1 to node A.
Return 1 if path exists else return 0.
NOTE:
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""
#Convert set to adj. list
#perform dfs

class Solution:
    #@param A : int -> last node
    #@param B : list of list of int -> connections
    #@return int -> 1 or 0
    def solve(self, A, B):
        adj = dict()
        for i in range(1, A + 1):
            adj[i] = list()
        
        for s, e in B:
            adj[s].append(e)

        self.A = A
        def dfs(node, visited, adjList):
            if node == self.A: return True
            visited.add(node)
            temp = False
            for c in adjList[node]:
                if c not in visited:
                    temp|= dfs(c, visited, adjList)
            return temp
        
        return 1 if dfs(1, set(), adj) else 0
                    


t = Solution()
A = 5
B = [  [1, 2],
        [2, 3], 
        [3, 4], 
        [4, 5] ]
print(t.solve(A, B))
