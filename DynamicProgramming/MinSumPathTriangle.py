"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1 is
"""

class Solution:
    def exist(self, i, j, arr):
        if i < len(arr) and j < len(arr[i]) and i > -1 and j > -1:
            return True
        return False

    #@param A: list of list of int
    #@return int -> minimum path sum
    def minimumTotal(self, A):
        if len(A) == 1: return A[0][0]
        for i in range(1, len(A)):
            for j in range(0, len(A[i])):
                ogi = A[i][j]
                A[i][j] = 1000001        #cannot be 1001, since total should be less than this number not just the number
                if self.exist(i-1, j, A):
                    A[i][j] = A[i-1][j] + ogi
                if self.exist(i-1, j-1, A):
                    A[i][j] = min(A[i][j], A[i-1][j-1] + ogi)
        return min(A[i])




B = [[1]]
A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
t = Solution()
print(t.minimumTotal(A))