"""
Given a graph with N nodes numbered 1 to N and M weighted edges. Given a binary array A of size N. A[i] = 1 if the ith node is special else 0.
Find the minimum distance of the special path between the 1st and the Nth node. Distance between two nodes is defined as the sum of the weight of edges in the path.
A special path is a path which visits alteast C non-special nodes and atleast D special nodes.
NOTE: A node or edge can occur multiple times in a special path. If no such path exists return -1.
"""
#not done

from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def solve(self, A, B, C, D):
        N = len(A)
        edges = defaultdict(list)
        for s, d, w in B:
            edges[s].append((w, d))
            edges[d].append((w, s))
        
        h = [(0, 1, int(A[0] == 0), int(A[0] == 1))]
        while h:
            #print(h)
            dis, node, c, d = heappop(h)
            if node == N and c >= C and d >= D: return dis
            for w, neigh in edges[node]:
                heappush(h, (dis + w, neigh, c + int(A[neigh - 1] == 0), d + int(A[neigh - 1] == 1)))
                
        return -1 


#class Solution:
#    def solve(self, A, B, C, D):


A = [ 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1 ]
B = [
  [1, 2, 8],
  [1, 3, 3],
  [1, 4, 12],
  [4, 5, 3],
  [3, 6, 3],
  [1, 7, 9],
  [7, 8, 4],
  [1, 9, 6],
  [2, 10, 11],
  [5, 11, 12],
  [9, 8, 6],
  [11, 4, 7],
  [11, 10, 7],
  [11, 2, 9]
]
C = 2 
D = 0

t = Solution()
print(t.solve(A, B, C, D))