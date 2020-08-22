"""
Given an array A of size N and Q queries. Perform following queries:
1 V 0 append V in the back of array.
2 X V set A[X] = V.
3 X 0 delete A[X]. Note: All element at back of X move forward to occupy void.
4 X Y find sum in range [X, Y].
NOTE: For the query of type 4 X Y, output the sum % 109 + 7.
"""
import sys
#sys.setrecursionlimit(10**7)
class SegmentTree:
    
    def build(self, array):
        if len(array) == 0:
            self.tree = None
            self.array = None
            return
        self.tree = [None] * (3*len(array))
        self.array = array
        def maketree(node, s, e):
            if s == e:
                self.tree[node] = self.array[s]
            else:
                mid = s + (e-s)//2
                l = 2 * node + 1
                r = 2 * node + 2
                maketree(l, s, mid)
                maketree(r, mid+1, e)
                self.tree[node] = (self.tree[l] + self.tree[r])%(10**9+7)
        maketree(0, 0, len(array)-1)

    def update(self, index, newval):
        def modifytree(node, s, e, index, val):
            if index < s or index > e: return
            elif s == e:
                self.tree[node] = val
            else:
                mid = s + (e-s)//2
                l = 2 * node + 1
                r = 2 * node + 2
                modifytree(l, s , mid, index, val)
                modifytree(r, mid+1, e, index, val)
                self.tree[node] = (self.tree[l] + self.tree[r])%(10**9+7)
        modifytree(0, 0, len(self.array)-1, index, newval)

    def query(self, l, r):
        def q(node, s, e, l, r):
            if l <= s and r >= e:
                return self.tree[node]
            elif r < s or l > e:
                return 0
            else:
                mid = s + (e-s)//2
                lc = 2 * node + 1
                rc = 2 * node + 2
                return (q(lc, s, mid, l, r)+q(rc, mid+1, e, l, r))%(10**9+7)
        return q(0, 0, len(self.array)-1, l, r)



class Solution:
    def displacement(self, l, r, skipTree):
        no = r-l+1
        s = l
        start = r
        end = len(skipTree.tree)-1
        ans = -1
        while start <= end:
            mid = start+(end-start)//2
            if mid-s-skipTree.query(s, mid)+1 <= no:
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans

    def disp(self, l, dis, skipTree):
        no = dis
        s = l
        start = l + dis -1
        end = len(skipTree.tree)-1
        ans = -1
        while start <= end:
            mid = start+(end-start)//2
            if mid-s-skipTree.query(s, mid)+1 <= no:
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans



    def solve(self, A, B):
        appendIndex = len(A)
        extra = 0
        for t,x,y in B:
            if t == 1:
                extra+=1
        for i in range(extra):
            A.append(0)

        skList = [0]*len(A)
        st = SegmentTree()
        skipTree = SegmentTree()
        st.build(A)
        skipTree.build(skList)
        

        ans = []
        for t, x, y in B:
            #print("Operation ({},{},{})".format(t, x, y))
            if t == 1:
                st.update(appendIndex, x)
                appendIndex+=1
            elif t == 2:
                x = x-1
                r = self.displacement(0, x, skipTree)
                st.update(r, y)
            elif t == 3:
                x = x-1
                r = self.displacement(0, x, skipTree)
                st.update(r, 0)
                skipTree.update(r, 1)
            elif t == 4:
                x = x-1
                y = y-1
                s = self.displacement(0, x, skipTree)
                r = self.disp(s, y-x+1, skipTree)
                ans.append(st.query(x, r))
            #print(A)
        return ans


"""
test = SegmentTree()
test.build([2])
print(test.tree)
test.build([])
#print(test.tree)
#print(test.query(0,5))

"""
t = Solution()
#A = [1] 
#B = [ [4, 1, 4], 
#       [3, 1, 0],
#       [1, 5, 0],
#       [4, 1, 2] ]

A = [ 6430, 648, 5697, 1429, 7620, 203, 8471, 5114, 3195, 1185, 665, 6829, 2418, 8657, 3784, 9168, 3139, 8696, 9509, 6963 ]
B = [[2, 6, 5663],
  [1, 6195, 0],
  [1, 5466, 0],
  [3, 16, 0],
  [2, 4, 2673],
  [3, 6, 0],
  [2, 14, 5389],
  [2, 7, 4883],
  [3, 12, 0],
  [4, 5, 14],
  [4, 3, 10],
  [1, 9153, 0],
  [3, 19, 0],
  [3, 7, 0],
  [2, 6, 3184],
  [2, 13, 609],
  [3, 12, 0],
  [3, 10, 0],
  [2, 3, 148],
  [4, 14, 14],
  [4, 5, 6],
  [2, 8, 4987],
  [3, 6, 0],
  [1, 2642, 0],
  [3, 15, 0],
  [3, 9, 0],
  [1, 4870, 0],
  [3, 9, 0],
  [3, 9, 0],
  [1, 3292, 0],
  [1, 6516, 0],
  [1, 8685, 0],
  [4, 4, 14],
  [2, 12, 4372],
  [1, 1184, 0],
  [3, 2, 0],
  [4, 8, 14],
  [4, 11, 11],
  [4, 8, 10],
  [4, 12, 13],
  [3, 8, 0],
  [2, 8, 2456],
  [4, 13, 15],
  [3, 7, 0],
  [2, 11, 8210],
  [1, 2360, 0],
  [3, 9, 0],
  [1, 3004, 0],
  [2, 2, 8549],
  [1, 5784, 0],
  [4, 6, 14],
  [1, 9023, 0],
  [4, 14, 15],
  [3, 9, 0],
  [1, 2743, 0],
  [3, 4, 0],
  [4, 5, 6],
  [1, 2398, 0],
  [3, 9, 0],
  [2, 3, 9452],
  [1, 9977, 0],
  [4, 4, 15],
  [4, 11, 12],
  [3, 7, 0],
  [3, 11, 0],
  [3, 6, 0],
  [2, 11, 8189],
  [1, 7286, 0],
  [3, 15, 0],
  [3, 1, 0],
  [2, 11, 5592],
  [2, 6, 9400],
  [3, 13, 0],
  [4, 4, 4],
  [3, 7, 0],
  [1, 2151, 0],
  [2, 9, 4085],
  [4, 2, 5],
  [4, 1, 1],
  [1, 7823, 0],
  [1, 5877, 0],
  [3, 2, 0],
  [4, 9, 9],
  [1, 4213, 0],
  [1, 2408, 0],
  [4, 8, 13],
  [3, 7, 0],
  [1, 7994, 0],
  [1, 6018, 0],
  [1, 9735, 0],
  [3, 16, 0]
]
print(t.solve(A, B))
