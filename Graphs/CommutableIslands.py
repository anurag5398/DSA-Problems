"""
There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.
We need to find bridges with minimal cost such that all islands are connected.
It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.
"""
#prims algo

from collections import defaultdict
import heapq
class Solution:
    #@param A: int
    #@param B: list of list of int
    #@return int
    def solve(self, A: int, B: list):
        paths = defaultdict(list)
        for s, d, w in B:
            paths[s].append((w, d))
            paths[d].append((w, s))
        
        heap = [(0, 1)]
        visited = set()
        total_distance = 0
        while heap:
            d, n = heapq.heappop(heap)
            if n not in visited:
                visited.add(n)
                total_distance+=d
                for c in paths[n]:
                    if c[1] not in visited:
                        heapq.heappush(heap, c)
        return total_distance




A = 4
B = [  [1, 2, 1],
        [2, 3, 2],
        [3, 4, 4],
        [1, 4, 3]   ]

t = Solution()
print(t.solve(A, B))