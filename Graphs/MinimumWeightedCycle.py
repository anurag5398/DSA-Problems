"""
Given an integer A, representing number of vertices in a graph.
Also you are given a matrix of integers B of size N x 3 where N represents number of Edges in a Graph and Triplet (B[i][0], B[i][1], B[i][2]) implies there is an undirected edge between B[i][0] and B[i][1] and weight of that edge is
B[i][2].
Find and return the weight of minimum weighted cycle and if there is no cycle return -1 instead.
NOTE: Graph may contain multiple edges and self loops.
"""
#for each edge, exclude that edge and see if any other path is
#possible between source and destination. If there is then cycle
#weight would be loop weight + excluded path weight
from collections import defaultdict
import heapq
class Solution:
    #@param dest : int -> node to reach
    #@param visited : set
    #@param heap : heapq
    #@param edges : defaultdict
    #@return int
    def path(self, dest, visited, heap, edges):
        while heap:
            w, n = heapq.heappop(heap)
            if n == dest:
                #print("Path exists with weight {}".format(w))
                return w
            visited.add(n)
            for c in edges[n]:
                if c[1] not in visited:
                    heapq.heappush(heap, (c[0] + w, c[1]))
        return -1

    #@param A : int -> total nodes
    #@param B : list of list of int -> edges
    def solve(self, A, B):
        ans = 99999
        edges = defaultdict(list)
        for s, d, w in B:
            if s == d:
                ans = min(w, ans)
            else:
                edges[s].append((w, d))
                edges[d].append((w, s))
        #        
        for s, d, w in B:
            if s != d:
                #print("current edge {} {} w {}".format(s, d, w))
                heap, visited = list(), set()
                visited.add(s)
                for c in edges[s]:
                    if c[1] != d:
                        heapq.heappush(heap, c)
                loopval = self.path(d, visited, heap, edges)
                if loopval != -1:
                    ans = min(loopval + w, ans)

        return ans if ans != 99999 else -1



A = 3
B = [  [1 ,2 ,2],
        [2 ,3 ,3]  ]

t = Solution()
print(t.solve(A, B))