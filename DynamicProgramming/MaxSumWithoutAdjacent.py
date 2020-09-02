"""
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.
"""
#option to select either current a[i] + i-2 or i-1
#dp[i] = max(dp[i-1], dp[i-2]+curr[i])
#base case is the first sum dp[0], but then dp[i-2] could not be defined for i = 1.
#solution: add a zero to orginal array
#further SC could be reduced by storing only last 2 dp values

class Solution:
    #param A : list of list of int
    #@return int
    def adjacent(self, A):
        prev, curr = 0, max(A[0][0], A[1][0])
        for i in range(1, len(A[0])):
            curr, prev = max(prev + max(A[0][i], A[1][i]), curr), curr
        return curr







A = [   [1, 2, 3, 4],
        [2, 3, 4, 5]    
     ]

t = Solution()
print(t.adjacent(A))