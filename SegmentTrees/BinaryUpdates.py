"""
Given an integer A denoting the size of the array consisting all ones.
You are given Q queries, for each query there are two integer x and y:
If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: There will atleast 1 query where value of x is 1.
"""

class SegmentTree:

    def build(self, array):
        self.tree = [None]*(4*len(array))
        self.array = array
        def make(node, s, e):
            if s == e:
                self.tree[node] = self.array[s]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                make(lc, s, mid)
                make(rc, mid+1, e)
                self.tree[node] = self.tree[lc] + self.tree[rc]
        make(0, 0, len(array)-1)

    def update(self, index):
        if self.array[index] == 0: return
        self.array[index] = 0
        def modify(node, s, e, index):
            if index < s or index > e: return
            elif s == e:
                self.tree[node] = 0
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                modify(lc, s, mid, index)
                modify(rc, mid+1, e, index)
                self.tree[node] = self.tree[lc] + self.tree[rc]
        modify(0, 0, len(self.array)-1, index)

    def query(self, k):
        if k > self.tree[0]: return -1
        def find(node, s, e, k):
            if s == e: return s
            mid = s + (e-s)//2
            lc = 2 * node + 1
            rc = 2 * node + 2
            if self.tree[lc] >= k:
                return find(lc, s, mid, k)
            else:
                return find(rc, mid+1, e, k-self.tree[lc])
        return find(0, 0, len(self.array)-1, k)


class Solution:
    #param A - int
    #param B - list int queries
    #return list int
    def solve(self, A, B):
        arr = [1]*A
        arr.insert(0, 0)
        st = SegmentTree()
        st.build(arr)
        ans = []
        for x, y in B:
            if x == 0:
                st.update(y)
            elif x == 1:
                ans.append(st.query(y))
        return ans

t = Solution()
A = 5
B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ]

print(t.solve(A, B))