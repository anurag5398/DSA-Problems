"""
A country consist of N cities connected by N - 1 roads. King of that country want to construct maximum number of roads such that the new country formed remains bipartite country.
Bipartite country is a country, whose cities can be partitioned into 2 sets in such a way, that for each road (u, v) that belongs to the country, u and v belong to different sets. Also, there should be no multiple roads between two cities and no self loops.
Return the maximum number of roads king can construct. Since the answer could be large return answer % 109 + 7.
NOTE: All cities can be visited from any city.
"""
#find how many cities can have 0 color
#and how many can have 1, by using the given edges
#all 0 can be connected to 1

from collections import defaultdict
MAX_SIZE = 10**9 + 7
class Solution:
    #@param node : int
    #@param color : list of int
    #@param adj : dict
    def fill(self, node, color, adj):
        for c in adj[node]:
            if color[c] == -1:
                color[c] = color[node]^1
                self.count[color[c]]+=1
                self.fill(c, color, adj)
    #@param A : int -> total cities
    #@param B : list of list of int -> roads
    def solve(self, A, B):
        color = [-1 for i in range(A + 1)]
        edge = defaultdict(list)
        for s, d in B:
            edge[s].append(d)
            edge[d].append(s)
        
        self.count = [1, 0]
        color[1] = 0
        self.fill(1, color, edge)
        tempval = (self.count[0] * self.count[1])%MAX_SIZE
        return (tempval-len(B))%MAX_SIZE
        


t = Solution()
A = 7
B = [
  [5, 3],
  [3, 1],
  [2, 1],
  [4, 1],
  [6, 1],
  [7, 1]
]
print(t.solve(A, B))
    
