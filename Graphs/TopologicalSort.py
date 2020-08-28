"""
Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.
Return the topological ordering of the graph and if it doesn't exist then return an empty array.
If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.
Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.
NOTE:
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""
#node with 0 in degree could be used first
#as we select nodes, its neighbours indegree will be reduced
#picking one by one until indegree becomes empty

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
