"""
Given an integer A, representing number of vertices in a graph.
Also you are given a matrix of integers B of size N x 3 where N represents number of Edges in a Graph and Triplet (B[i][0], B[i][1], B[i][2]) implies there is an undirected edge between B[i][0] and B[i][1] and weight of that edge is
B[i][2].
Find and return the weight of minimum weighted cycle and if there is no cycle return -1 instead.
NOTE: Graph may contain multiple edges and self loops.
"""
#NOT DONE
from collections import defaultdict
import heapq
class Solution:
    def bfs(self, heap, visited, edges):
        if not heap: return
        d, n, p = heapq.heappop(heap)
        #print("d {} n {} p {}".format(d, n, p))
        if n in visited:
            self.bfs(heap, visited, edges)
        else:
            visited.add(n)
            #print(visited)
            for c, w in edges[n]:
                #print(heap)
                if c not in visited:
                    heapq.heappush(heap, (d + w, c, n))
                elif c == self.current and p != self.current:
                    print("loop {} {} dis {}".format(n, self.current, d + w))
                    return
            self.bfs(heap, visited, edges)
                

    def solve(self, A, B):
        edges = defaultdict(list)
        for s, d, w in B:
            edges[s].append((d, w))
            edges[d].append((s, w))
        print(edges)
        self.loop = 9999
        for i in range(1, A + 1):
            self.current = i
            heap = list()
            heap.append((0, i, -1))
            self.bfs(heap, set(), edges)



A = 4
B = [  [1 ,2 ,2],
        [2 ,3 ,3],
        [3 ,4 ,1],
        [4 ,1 ,4],
        [1 ,3 ,15]  ]

t = Solution()
print(t.solve(A, B))