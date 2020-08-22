"""
Given a binary string A of size N and an integer matrix B of size Q x 3.
Matrix B has Q queries:
For queries of type B[i][0] = 1, flip the value at index B[i][1] in A if and only if the value at that index is 0 and return -1.
For queries of type B[i][0] = 0, Return the value of the binary string from index B[i][1] to B[i][2] modulo 3.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.
"""
import sys
sys.setrecursionlimit(10**5)
def fastpow(power):
    if power < 1: return 1
    else: return pow(2,power,3)

class SegmentTree:

    def build(self, string):
        self.array = list(string)
        self.tree = [None]*(4*len(string))
        def create(node, s, e):
            if s == e:
                self.tree[node] = int(self.array[s])
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                create(lc, s, mid)
                create(rc, mid+1, e)
                multiplier = fastpow(e-mid)
                self.tree[node] = (self.tree[lc]*multiplier+self.tree[rc])
        create(0, 0, len(string)-1)


    def update(self, index):
        if self.array[index] == 1: return
        self.array[index] = 1
        def modify(node, s, e, index):
            if index < s or index > e: return
            if s == e:
                self.tree[node] = 1
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                modify(lc, s, mid, index)
                modify(rc, mid+1, e, index)
                multiplier = fastpow(e-mid)
                self.tree[node] = (self.tree[lc]*multiplier+self.tree[rc])%3
        modify(0, 0, len(self.array)-1, index)

    def query(self, l, r):
        print("query for {} {}".format(l, r))
        def find(node, s, e, l, r):
            if r < s or l > e: return 0
            if l <= s and r >= e: return self.tree[node]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                p1 = find(lc, s, mid, l, r)
                p2 = find(rc, mid+1, e, l, r)
                print("p1{} p2{} s{} mid{} e{} l{} r{}".format(p1, p2, s, mid, e, l, r))
                if min(e,r)-mid > 0:
                    multiplier = p1<<(min(e,r)-mid)
                else:
                    multiplier = p1<<(e-mid)
                return multiplier + p2
        return find(0, 0, len(self.array)-1, l, r)


class Solution:
    # @param A : string
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        st = SegmentTree()
        st.build(A)
        print(st.tree)
        ans = []
        for t, x, y in B:
            if t == 1:
                st.update(x-1)
                ans.append(-1)
            elif t == 0:
                ans.append(st.query(x-1, y-1))
                break
        return ans



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


"""
s = SegmentTree()
a = "10010"
s.build(a)
print(s.tree)
print(s.query(0, 4))
s.update(2)
print(s.tree)
print(s.query(0, 4))
"""