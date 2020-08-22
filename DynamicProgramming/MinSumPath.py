"""
Given a M x N grid A of integers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Return the minimum sum of the path.
NOTE: You can only move either down or right at any point in time.
"""

class Solution:
    #@param A : 2D list of int
    #@return int : min path sum
    def minPathSum(self, A):
        cost = [[0 for i in range(len(A[0]))] for i in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A[0])):

                if i == 0 and j == 0:
                    cost[i][j] = A[i][j]
                
                elif i == 0:
                    cost[i][j] = cost[i][j-1] + A[i][j]
                
                elif j == 0:
                    cost[i][j] = cost[i-1][j] + A[i][j]
                
                else:
                    cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + A[i][j]

        return cost[i][j]


t = Solution()
A = [
       [1, 3, 2],
       [4, 3, 1],
       [5, 6, 1]
     ]
print(t.minPathSum(A))