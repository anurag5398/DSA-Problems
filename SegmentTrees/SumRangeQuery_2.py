

class SegmentTree:
    def __init__(self):
        self.MAX_SIZE = 20

    def build(self, array):
        self.tree = [None] * (4*len(array))
        def create(node, s, e, array):
            if s == e:
                self.tree[node] = array[s]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                create(lc, s, mid, array)
                create(rc, mid+1, e, array)
                self.tree[node] = (self.tree[lc]+self.tree[rc])%(10**9+7)
        create(0, 0, len(array)-1, array)

    def update(self, index, value):
        def modify(node, s, e, index, value):
            if index < s or index > e: return
            if s == e:
                self.tree[node] = value
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                modify(lc, s, mid, index, value)
                modify(rc, mid+1, e, index, value)
                self.tree[node] = (self.tree[lc]+self.tree[rc])%(10**9+7)
        modify(0, 0, self.MAX_SIZE-1, index, value)

    def query(self, l, r):
        def search(node, s, e, l, r):
            if r < s or l > e: return 0
            elif l <= s and r >= e: return self.tree[node]
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                return search(lc, s, mid, l, r)+search(rc, mid+1, e, l, r)
        return search(0, 0, self.MAX_SIZE-1, l, r)%(10**9+7)

    def sumIndex(self, k):
        if k > self.tree[0]: return -1
        def find(node, s, e, k):
            if s == e: return s
            mid = s + (e-s)//2
            lc = 2 * node + 1
            rc = 2 * node + 2
            if k <= self.tree[lc]:
                return find(lc, s, mid, k)
            else:
                return find(rc, mid+1, e, k-self.tree[lc])
        return find(0, 0, self.MAX_SIZE-1, k)

                


class Solution:
    def __init__(self):
        self.MAX_SIZE = 20
    #A - input array - int
    #B - 3 X N - query array
    #return int array
    def solve(self, A, B):
        indexArr = [1] * (self.MAX_SIZE-1)
        indexArr.insert(0, 0)
        A.insert(0, 0)
        appendIndex = len(A)
        A = A + ([0]*(self.MAX_SIZE-appendIndex))
        
        st = SegmentTree()
        st.build(A)

        Ist = SegmentTree()
        Ist.build(indexArr)

        ans = []
        for t, x, y in B:
            if t == 1:
                st.update(appendIndex, x)
                appendIndex+=1
            elif t == 2:
                r = Ist.sumIndex(x)
                st.update(r, y)
            elif t == 3:
                r = Ist.sumIndex(x)
                Ist.update(r, 0)
                st.update(r, 0)
            elif t == 4:
                s = Ist.sumIndex(x)
                r = Ist.sumIndex(y)
                ans.append(st.query(s, r))

        return ans


t = Solution()
A = [1, 2, 5, 3, 4] 
B = [ [4, 2, 4], 
       [3, 3, 0],
       [1, 6, 0],
       [4, 3, 5] ]
print(t.solve(A, B))

