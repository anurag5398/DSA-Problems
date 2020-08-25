"""
Given a undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that there is an edge between B[i][0] and B[i][1].
Find whether the given graph is bipartite or not.
A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
"""
#for bipartite graphs, we could use 2 colors to color it
#so we will alternatively give 1 and 0 color, if any adj. node has same color then
#can't be bipartite

import sys
sys.setrecursionlimit(10**7)
class Solution:
    #@param node: int -> vertice
    #@param edges: dict -> edges
    #@param color: list of int -> color of node
    #@return boolean
    def bipartite(self, node, edges, color):
        for c in edges[node]:
            #print("currently node {} color {} child {} color {}".format(node, color[node], c, color[c]))
            if color[c] == -1:
                color[c] = color[node]^1
                self.bipartite(c, edges, color)
            else:
                if color[c] == color[node]:
                    self.flag = False
        return

    #@param A : int -> number of nodes
    #@param B : list of list of int -> edges
    #@return int -> 1/0
    def solve(self, A, B):
        edges = dict()
        for s, d in B:
            if s not in edges:
                edges[s] = [d]
            else:
                edges[s].append(d)
            if d not in edges:
                edges[d] = [s]
            else:
                edges[d].append(s)
        color = [-1 for i in range(A)]
        first = B[0][0]
        color[first] = 0
        self.flag = True
        for i in range(len(B)):
            self.bipartite(B[i][0], edges, color)
        if self.flag:
            return 1
        else: return 0
t = Solution()
A = 96
B = [
  [11, 68],
  [4, 76],
  [29, 78],
  [14, 59],
  [2, 92],
  [17, 81],
  [16, 48],
  [20, 93],
  [71, 93],
  [74, 78],
  [19, 67],
  [11, 48],
  [19, 71],
  [0, 87],
  [39, 75],
  [32, 72],
  [52, 89],
  [1, 95],
  [61, 77],
  [34, 94],
  [48, 66],
  [9, 39],
  [21, 30],
  [1, 68],
  [15, 76],
  [22, 88],
  [64, 94],
  [43, 51],
  [22, 29],
  [10, 76],
  [59, 78],
  [25, 28],
  [92, 94],
  [11, 52],
  [28, 78],
  [27, 90],
  [30, 71],
  [15, 30],
  [14, 78],
  [35, 68],
  [32, 91],
  [10, 46],
  [60, 79],
  [11, 58],
  [0, 16]
]
print(t.solve(A, B))
