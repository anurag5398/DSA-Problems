"""
Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""

class Solution:

    def uniquePathsWithObstacles(self, A):
        #@param A : 2D int list
        #@return int
        if A[0][0] == 1: return 0
        temp = [[0] * (len(A[0])+1) for i in range(len(A)+1)]
        temp[1][1] = 1
        for i in range(1, len(temp)):
            for j in range(1, len(temp[0])):
                if A[i-1][j-1] == 0 and i+j > 2:
                    temp[i][j] = temp[i-1][j] + temp[i][j-1]
        return temp[i][j]


t = Solution()
A = [[0,0,0],
    [1,1,1],
    [0,0,0]
]
print(t.uniquePathsWithObstacles(A))