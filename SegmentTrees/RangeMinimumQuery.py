"""
Given an integer array A of size N.
You have to perform two types of query, in each query you are given three integers x,y,z.
If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.
"""

class SegmentTrees:
    
    def buildtree(self, array):
        self.array = array
        print(len(array))
        self.tree = [None]*(3*len(array))
        def build(node, s, e):
            if s == e:
                self.tree[node] = self.array[s]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                build(lc, s, mid)
                build(rc, mid+1, e)
                self.tree[node] = min(self.tree[lc], self.tree[rc])
        build(0, 0, len(array)-1)

    def query(self, l, r):
        def findMin(node, s, e, l, r):
            if r < s or l > e: return float('inf')
            elif l <= s and r >= e: return self.tree[node]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                return min(findMin(lc, s, mid, l, r), findMin(rc, mid+1, e, l, r))
        return findMin(0, 0, len(self.array)-1, l, r)

    def update(self, index, val):
        def modifyIndex(node, s, e, index, val):
            if index < s or index > e: return
            elif s == e:
                self.tree[node] = val
                return
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                modifyIndex(lc, s, mid, index, val)
                modifyIndex(rc, mid + 1, e, index, val)
                self.tree[node] = min(self.tree[lc], self.tree[rc])
        modifyIndex(0, 0, len(self.array)-1, index, val)

            

class Solution:
    def solve(self, A, B):
        st = SegmentTrees()
        st.buildtree(A)
        ans = []
        for t, x, y in B:
            if t == 0:
                st.update(x-1, y)
            elif t == 1:
                ans.append(st.query(x-1, y-1))
        return ans

"""
t = SegmentTrees()
t.buildtree([5,4,5,7])
print(t.query(2,4))
t.update(1, 0)
print(t.query(2,3))
"""

s = Solution()
A = [ 18, 10, 1, 20, 25, 4, 9, 13, 15, 6, 21, 7 ]
B = [
  [1, 8, 12],
  [0, 4, 7],
  [1, 1, 3],
  [1, 5, 11],
  [1, 3, 9],
  [1, 7, 12],
  [1, 7, 10],
  [0, 12, 20]
]
print(s.solve(A, B))