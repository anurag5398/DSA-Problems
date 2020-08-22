"""
Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.
Find the maximum number of chocolates that kid can eat in A units of time.
NOTE:
floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7
"""
class MaxHeap:
    def downheapify(self, index):
        lc = 2 * index + 1
        rc = 2 * index + 2
        #print("Downheap index {} lc {} rc {}")
        #print("index {} lc {} rc {} size {} tree {}".format(index, lc, rc, self.size, self.tree))
        if lc < self.size and self.tree[lc] > self.tree[index] and rc < self.size and self.tree[lc] >= self.tree[rc]:
            self.tree[lc], self.tree[index] = self.tree[index], self.tree[lc]
            self.downheapify(lc)
        elif lc < self.size and self.tree[lc] > self.tree[index] and rc >= self.size:
            self.tree[lc], self.tree[index] = self.tree[index], self.tree[lc]
            self.downheapify(lc)

        elif rc < self.size and self.tree[rc] > self.tree[index] and self.tree[rc] >= self.tree[lc]:
            self.tree[rc], self.tree[index] = self.tree[index], self.tree[rc]
            self.downheapify(rc)

    def upheapify(self, index):
        current = index
        parent = (current-1)//2
        #print("upheapify starting now with self.tree {} current{} parent {}".format(self.tree, current, parent))
        while current != 0 and self.tree[parent] < self.tree[current]:
            #print("swapiing tree[parent] {}  < tree[current {}".format(self.tree[parent], self.tree[current]))
            self.tree[current], self.tree[parent] = self.tree[parent], self.tree[current]
            current = parent
            parent = (current-1)//2
        #print("Heapify Completed tree {}".format(self.tree))

    def build(self, array):
        self.tree = array
        self.size = len(array)

        for i in range(self.size):
            index = self.size-i-1
            self.upheapify(index)

    def removeMax(self):
        self.tree[0], self.tree[self.size-1] = self.tree[self.size-1], self.tree[0]
        self.tree.pop()
        self.size-=1
        self.downheapify(0)
        #print("max removed ", self.tree)

    def insert(self, val):
        self.tree.append(val)
        self.size+=1
        self.upheapify(self.size-1)
        #print("Inserted ",self.tree)


class Solution:
    # @param A : integer
	# @param B : list of integers
	# @return an integer
    def nchoc(self, A, B):
        mH = MaxHeap()
        mH.build(B)
        #print(mH.tree)
        ans = 0
        for i in range(A):
            temp = mH.tree[0]
            ans = (ans + temp)%(10**9+7)
            mH.removeMax()
            #print("removed tree ",mH.tree)
            mH.insert(temp//2)
            #print(mH.tree)
        return ans%(10**9+7)


import heapq

class Solution2:
    def nchoc(self, A, B):
        for i in range(len(B)):
            B[i] = -B[i]
        
        heapq.heapify(B)
        ans = 0
        for i in range(A):
            x = heapq.heappop(B)
            x = -x
            ans = (ans+x)%(10**9+7)
            temp = x//2
            temp = -temp
            heapq.heappush(B, temp)
        return ans


"""
mh = MaxHeap()
mh.build([5,6,7,10,20])
print(mh.tree)
mh.insert(40)
print(mh.tree)
mh.removeMax()
print(mh.tree)
mh.removeMax()
print(mh.tree)
"""
t = Solution2()
A = 5
B = [ 2, 4, 6, 8, 10 ]
print(t.nchoc(A, B))