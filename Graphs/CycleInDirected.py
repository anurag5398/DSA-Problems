"""
Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].
Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.
NOTE:
The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""
#Unlike undirected, we can't assume a cycle is present is we land on the same node twice
#we have to check if the current path has any repetitive node
#maintain 2 array visited and currentpathvisited
from collections import defaultdict
class Solution:
    #@param node : int
    #@param visited : list of int
    #@param currentVisited : list of int
    def dfs(self, node, visited, currentVisited):

        visited[node] = True
        currentVisited[node] = True

        for c in self.edges[node]:
            if visited[c] is False:
                if self.dfs(c, visited, currentVisited):
                    return True
            elif currentVisited[c] is True:
                return True
        currentVisited[node] = False
        

    #@param A : int -> no of nodes
    #@param B : list of list of int -> edges
    def solve(self, A, B):
        self.edges = defaultdict(list)
        for s, d in B:
            self.edges[s].append(d)

        visited, currentVisited = [False] * (A + 1), [False] * (A + 1)
        for i in range(1, A + 1):
            if visited[i] is False:
                if self.dfs(i, visited, currentVisited): return 1
        return 0  


A = 5
B = [  [1, 2], 
        [4, 1], 
        [2, 4],
        [3, 4], 
        [5, 2], 
        [1, 3] ]

t = Solution()
print(t.solve(A, B))