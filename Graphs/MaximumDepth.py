"""
Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.
You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.
Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X.

NOTE:
Level and Depth of the root is considered as 0.
It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
Please read the input format for more clarification.
"""

from collections import defaultdict, deque

class Solution:
    #@param v : int
    #@param level : list of int
    #@return int
    def find(self, v, level):
        s, e = 0, level[0] - 1
        arr = level[1]
        ans = -1
        #print(s, e, arr)
        while s <= e:
            mid = s + (e - s)//2
            if arr[mid] < v:
                s = mid + 1
            else:
                ans = arr[mid]
                e = mid - 1
        return ans

        

    #@param A : int
    #@param B, C : list of int
    #@param D : list of int
    #@param E, F : list of int
    def solve(self, A, B, C, D, E, F):
        edges = defaultdict(list)
        for s, d in zip(B, C):
            edges[s].append(d)
            edges[d].append(s)
        
        q = deque()
        level = defaultdict(list)
        #(node, distance, parent)
        q.append((1, 0, -1))
        while q:
            n, d, p = q.popleft()
            level[d].append(D[n-1])
            for c in edges[n]:
                if c != p:
                    q.append((c, d + 1, n))

        for k in level:
            level[k] = (len(level[k]), sorted(level[k]) )
        s = len(level)
        ans = []
        for l, v in zip(E, F):
            ans.append(self.find(v, level[l%s]))
        return ans
            

        
A = 5
B = [1, 4, 3, 1]
C = [5, 2, 4, 4]
D = [7, 38, 27, 37, 1]
E = [1, 1, 2]
F = [32, 18, 26]
t = Solution()
print(t.solve(A, B, C, D, E, F))