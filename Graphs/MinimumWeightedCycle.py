"""
Given an integer A, representing number of vertices in a graph.
Also you are given a matrix of integers B of size N x 3 where N represents number of Edges in a Graph and Triplet (B[i][0], B[i][1], B[i][2]) implies there is an undirected edge between B[i][0] and B[i][1] and weight of that edge is
B[i][2].
Find and return the weight of minimum weighted cycle and if there is no cycle return -1 instead.
NOTE: Graph may contain multiple edges and self loops.
"""
from collections import defaultdict
class Solution:
    def findmin(self, A, inD, out):
        minv, mink = 99999, 99999
        for k, v in inD.items():
            if v < minv:
                mink, minv = k, v
            elif v == minv and k < mink:
                mink = k

        for c in out[mink]:
            inD[c]-=1
        return mink, minv
    #@param A : int -> total nodes
    #@param B : list of list of int -> edges
    def solve(self, A, B):
        inD, outD = dict(), defaultdict(list)
        for i in range(1, A + 1):
            inD[i] = 0
        for s, d in B:
            outD[s].append(d)
            inD[d]+=1
        visited = set()
        ans = []
        k, v = self.findmin(A, inD, outD)
        if v != 0: return []
        visited.add(k)
        ans.append(k)
        inD.pop(k)
        
        while inD:
            k, v = self.findmin(A, inD, outD)
            visited.add(k)
            ans.append(k)
            inD.pop(k)
        return ans





t = Solution()
A = 6
B = [  [6, 3] ,
        [6, 1] ,
        [5, 1] ,
        [5, 2] ,
        [3, 4] ,
        [4, 2] ]
print(t.solve(A, B))
