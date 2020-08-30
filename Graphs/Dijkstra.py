"""
Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.
You have to find an integer array D of size A such that:
=> D[i] : Shortest distance form the C node to node i.
=> If node i is not reachable from C then -1.
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
"""
from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    #@param A : int
    #@param B : list of list of int
    #@param C : int
    #@return list of int
    def  solve(self, A, B, C):
        nodes = [-1 for _ in range(A)]
        adj = defaultdict(list)
        for s, d, w in B:
            adj[s].append((w, d))
            adj[d].append((w, s))
        #print(adj)
        h = []
        heappush(h, (0, C))
        visited = set()
        visited.add(C)
        while h:
            w, n = heappop(h)
            visited.add(n)
            if nodes[n] == -1: nodes[n] = w
            else: nodes[n] = min(nodes[n], w)
            for tw, tn in adj[n]:
                if tn not in visited:
                    heappush(h, (w + tw, tn))
        return nodes


A = 5
B = [   [0, 3, 4],
        [2, 3, 3] ,
        [0, 1, 9] ,
        [3, 4, 10] ,
        [1, 3, 8]  ] 
C = 4
t = Solution()
print(t.solve(A, B, C))
