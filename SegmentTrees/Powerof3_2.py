class SegmentTree:

    def build(self, string):
        self.array = [int(i) for i in string]
        self.tree = [None]*(4*len(string))
        def make(node, s, e):
            if s == e:
                self.tree[node] = self.array[s]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                make(lc, s, mid)
                make(rc, mid+1, e)
                left = self.tree[lc]<<(e-mid)
                self.tree[node] = left + self.tree[rc]
        make(0, 0, len(string)-1)

class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        st = SegmentTree()
        st.build(A)
        print(st.tree)
        ans = []
        """
        for t, x, y in B:
            if t == 1:
                st.update(x-1)
                ans.append(-1)
            elif t == 0:
                ans.append(st.query(x-1, y-1))
        return ans
        """



A = "0100111001"
B = [
  [0, 1, 2],
  [1, 6, -1],
  [0, 5, 6],
  [1, 2, -1],
  [0, 7, 9],
  [0, 1, 5],
  [1, 2, -1],
  [1, 6, -1],
  [1, 6, -1],
  [1, 3, -1],
  [0, 8, 9],
  [1, 3, -1],
  [1, 3, -1],
  [1, 10, -1],
  [0, 3, 5],
  [1, 9, -1],
  [1, 5, -1],
  [1, 2, -1],
  [0, 5, 9],
  [0, 1, 9],
  [1, 4, -1],
  [1, 4, -1],
  [1, 4, -1],
  [0, 5, 8],
  [0, 3, 6],
  [1, 6, -1],
  [1, 5, -1],
  [0, 3, 5],
  [0, 3, 9],
  [1, 1, -1]
]

t = Solution()
print(t.solve(A, B))
