"""
Sheldon lives in a country with A cities (numbered from 1 to A) and B bidirectional roads.
Roads are denoted by integer array D, E and F of size M, where D[i] and E[i] denotes the cities and F[i] denotes the distance between the cities.
Now he has many lectures to give in the city and is running short of time, so he asked you C queries, for each query i, find the shortest distance between city G[i] and H[i].
If the two cities are not connected then the distance between them is assumed to be -1.
"""
from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    #@param A, B, C : int
    #@param D, E, F : list of int
    #@param G, H : list of int
    def solve(self, A, B, C, D, E, F, G, H):
        distance = [[float('inf') for _ in range(A + 1)] for _ in range(A + 1)]
        print(distance)
        for s, d, w in zip(D, E, F):
            distance[s][d] = w
            distance[d][s] = w
        
        for i in range(A + 1):
            distance[i][i] = 0
        for i in range(A + 1):
            distance[0][i] = 0
            distance[i][0] = 0
        
        for k in range(1, A + 1):
            for i in range(1, A + 1):
                for j in range(1, A + 1):
                    if i != k or j != k or i != j:
                        distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
        
        ans = list()
        for s, d in zip(G, H):
            path = min(distance[s][d], distance[d][s])
            if path == float('inf'): ans.append(-1)
            else: ans.append(path)
        return ans

class Solution2:
    def solve(self, A, B, C, D, E, F, G, H):
        edges = defaultdict(list)
        for s, d, w in zip(D, E, F):
            edges[s].append((w, d))
            edges[d].append((w, s))
        
        distance = [[0 for _ in range(A + 1)] for _ in range(A + 1)]
        #note: [i][i] will have garbage valuw

        for node in range(1, A + 1):
            heap = [(0, node)]
            visited = set()
            while heap:
                dis, n = heappop(heap)
                if distance[node][n] == 0:
                    distance[node][n] = dis
                    for c in edges[n]:
                        if distance[node][c[1]] == 0:
                            heappush(heap, (dis + c[0], c[1]))
        ans = list()
        for s, d in zip(G, H):
            if s == d: ans.append(0)
            elif distance[s][d] == 0: ans.append(-1)
            else: ans.append(distance[s][d])
        return ans    



                        
                    





A = 4
B = 6
C = 2
D = [1, 2, 3, 2, 4, 3]
E = [2, 3, 4, 4, 1, 1]
F = [4, 1, 1, 1, 1, 1]
G = [1, 1]
H = [2, 3]
t = Solution2()
print(t.solve(A, B, C, D, E, F, G, H))