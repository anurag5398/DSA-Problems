"""
Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

class Solution:
    def histogram(self, arr):
        ls, rs = [0] * len(arr), [0] * len(arr)
        lstack, rstack = [], []
        for i in range(len(arr)):
            while len(lstack) > 0 and arr[lstack[-1]] >= arr[i]:
                lstack.pop()
            if len(lstack) == 0: 
                ls[i] = -1
                lstack.append(i)
            else: 
                ls[i] = lstack[-1]
                lstack.append(i)


            j = len(arr)-i-1
            while len(rstack) > 0 and arr[rstack[-1]] >= arr[j]:
                rstack.pop()
            if len(rstack) == 0:
                rs[j] = len(arr)
                rstack.append(j)
            else:
                rs[j] = rstack[-1]
                rstack.append(j)
        size = 0
        for i in range(len(arr)):
            size = max( (rs[i] - ls[i] - 1) * arr[i], size )

        return size

    #@param A: list of list of int -> 1/0
    #@return int -> max rectangle size
    def maximalRectangle(self, A):
        for j in range(len(A[0])):
            t = 0
            for i in range(len(A)):
                if A[i][j] == 1:
                    t+=1
                    A[i][j] = t
                else:
                    t = 0
        print(A)
        maxarea = 0
        for i in range(len(A)):
            maxarea = max( self.histogram(A[i]), maxarea )
        return maxarea

        
        



A = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 0, 0, 0],
]
t = Solution()
print(t.maximalRectangle(A))
B = [3,6,4,2,7]
#print(t.histogram(B))