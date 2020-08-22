"""
Given a weighted undirected graph having A nodes, a source node C and destination node D.
Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.
You are expected to do it in Time Complexity of O(A + M).
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.
"""
from collections import deque
class Solution:
    #@param A : int -> total nodes
    #@param B : list of list of int -> weighted connections
    #@param C : int -> source
    #@param D : int -> destination
    #@return int -> distance b/w C and D
    def solve(self, A, B, C, D):
        path = dict()
        for i in range(A): path[i] = []
        for s, d, w in B:
            path[s].append((d, w))
            path[d].append((s, w))

        visited = set()
        q = deque([])
        q.append((C, 0, 0))
        visited.add(C)

        while q:
            print(q)
            n, d, td = q.popleft()
            if d > 1:
                q.append((n, d-1, td+1))
                continue
            if n == D: return td
            for c in path[n]:
                if c[0] not in visited:
                    q.append((c[0], c[1], td+1))
                    visited.add(c[0])
        return -1



A = 106
B = [
  [38, 45, 2],
  [67, 88, 2],
  [43, 48, 2],
  [11, 105, 1],
  [1, 87, 2],
  [21, 33, 1],
  [6, 78, 1],
  [55, 84, 2],
  [77, 97, 2],
  [28, 93, 2],
  [41, 63, 2],
  [3, 79, 2],
  [13, 57, 2],
  [3, 34, 2],
  [45, 81, 2],
  [44, 64, 1],
  [38, 55, 1],
  [27, 83, 1],
  [44, 103, 1],
  [31, 93, 1],
  [57, 66, 2],
  [22, 42, 2],
  [25, 75, 2],
  [1, 79, 1],
  [18, 71, 2],
  [10, 99, 2],
  [35, 78, 1],
  [30, 102, 1],
  [31, 47, 1],
  [82, 84, 2],
  [21, 24, 2],
  [17, 60, 1],
  [52, 95, 1],
  [42, 52, 1],
  [21, 45, 1],
  [85, 86, 1],
  [83, 88, 1],
  [7, 53, 1],
  [2, 30, 1],
  [58, 67, 2],
  [21, 103, 1],
  [84, 99, 2],
  [42, 56, 2],
  [23, 97, 1],
  [74, 96, 2],
  [34, 59, 1],
  [21, 66, 1],
  [18, 82, 1],
  [39, 91, 2],
  [13, 36, 2],
  [54, 83, 2],
  [21, 92, 2],
  [40, 92, 2],
  [13, 22, 2],
  [5, 53, 1],
  [33, 94, 2],
  [39, 44, 2],
  [53, 62, 2],
  [12, 66, 2],
  [37, 92, 1],
  [32, 68, 1],
  [22, 47, 1],
  [50, 102, 1],
  [21, 49, 1],
  [69, 84, 2],
  [32, 41, 2],
  [75, 104, 1],
  [67, 79, 2],
  [16, 85, 1],
  [40, 56, 2],
  [27, 69, 1],
  [14, 40, 2],
  [39, 47, 2],
  [40, 61, 1],
  [22, 102, 1],
  [21, 69, 2],
  [34, 102, 1],
  [2, 7, 2],
  [19, 30, 2],
  [57, 82, 2],
  [37, 46, 1],
  [3, 28, 1],
  [22, 93, 1],
  [54, 70, 1],
  [26, 103, 1],
  [61, 87, 1],
  [53, 90, 1],
  [77, 102, 2],
  [48, 57, 1],
  [72, 73, 2],
  [25, 38, 2],
  [41, 67, 2],
  [17, 103, 1],
  [44, 71, 1],
  [11, 30, 1],
  [14, 16, 2],
  [44, 83, 1],
  [50, 101, 1],
  [15, 36, 1],
  [87, 90, 2],
  [53, 95, 2],
  [81, 94, 2],
  [5, 85, 1],
  [56, 99, 2],
  [71, 80, 1],
  [2, 24, 1],
  [14, 72, 1],
  [53, 80, 1]
]
C = 63
D = 92
t = Solution()
print(t.solve(A, B, C, D))
