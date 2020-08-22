"""
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
Given a 2D array of integers A of size M x N. Find and return the knight's minimum initial health so that he is able to rescue the princess.
"""

class Solution:
    #@param curr: int -> value of previous cell
    #@param new: int -> value of next cell
    def calc(self, curr, new):
        curr+= -new
        return curr if curr > 1 else 1

    #@param A : list of list of int
    #@return int -> minimum health
    def calculateMinimumHP(self, A):
        n, m = len(A), len(A[0])
        dp = [[0 for i in range(m)] for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                if i == n-1 and j == m-1:
                    dp[i][j] = self.calc(1, A[i][j])

                elif i == n-1:
                    dp[i][j] = self.calc(dp[i][j+1], A[i][j])

                elif j == m-1:
                    dp[i][j] = self.calc(dp[i+1][j], A[i][j])
                
                else:
                    dp[i][j] = self.calc(min(dp[i][j+1], dp[i+1][j]), A[i][j])
        return dp[i][j]



t = Solution()
A = [ 
       [1, -1, 0],
       [-1, 1, -1],
       [1, 0, -1]
     ]
t.calculateMinimumHP(A)

